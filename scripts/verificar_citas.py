"""Verifica que cada cita literal del mapa esté en la página que se indica.

Proceso:
  1. Extrae el texto de los dos tomos del Libro Blanco con pdftotext (Poppler), página por página.
  2. Lee las citas guardadas en index.html (bloque JSON con id "lb-data").
  3. Busca cada cita en la página citada (o en la página siguiente, si la cita cruza de una a otra).
  4. Revisa que las flechas, las políticas y los recorridos apunten a elementos que existen.

Uso:
  python scripts/verificar_citas.py RUTA/libro_blanco_1.pdf RUTA/libro_blanco_2.pdf

Los PDF no están en el repositorio (tienen derechos reservados de EsSalud). Se descargan de:
  https://www.essalud.gob.pe/transparencia/libro_blanco/libro_blanco_1.pdf
  https://www.essalud.gob.pe/transparencia/libro_blanco/libro_blanco_2.pdf

Paquetes: solo la biblioteca estándar de Python (json, re, subprocess, pathlib, sys, tempfile).
Requiere el programa pdftotext en el PATH (viene con Poppler o con Git para Windows).
"""

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DESPLAZAMIENTO = 2  # página del PDF = página impresa + 2, en ambos tomos
INDEX = Path(__file__).resolve().parent.parent / "index.html"


# --- Proceso 1: texto por página -------------------------------------------------
def paginas(pdf: Path) -> dict[int, str]:
    """Devuelve {número de página del PDF: texto normalizado}."""
    with tempfile.TemporaryDirectory() as tmp:
        salida = Path(tmp) / "texto.txt"
        subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), str(salida)], check=True)
        bloques = salida.read_text(encoding="utf-8").split("\f")
    return {i + 1: normalizar(b) for i, b in enumerate(bloques)}


def normalizar(texto: str) -> str:
    """Une palabras cortadas con guion al final de línea, colapsa espacios y pasa a minúsculas."""
    texto = texto.replace("­", "")
    texto = re.sub(r"-\s*\n\s*", "", texto)
    texto = re.sub(r"\s+", " ", texto)
    texto = texto.replace("“", '"').replace("”", '"').replace("’", "'")
    return texto.strip().lower()


# --- Proceso 2: citas del mapa ---------------------------------------------------
def citas(datos: dict):
    """Recorre todas las citas literales con su tomo, página impresa y lugar del mapa."""
    for s in datos["stats"]:
        yield s["c"]["t"], s["c"]["p"], s["q"], "cifra de cabecera"
    for s in datos["thesis"]:
        yield s["q"]["t"], s["q"]["p"], s["q"]["q"], "tesis"
    for nodo in datos["nodes"]:
        for q in nodo["quotes"]:
            yield q["t"], q["p"], q["q"], nodo["id"]
    for p in datos["pols"]:
        yield p["obj"]["t"], p["obj"]["p"], p["obj"]["q"], p["id"]
    for d in datos["decs"]:
        yield d["q"]["t"], d["q"]["p"], d["q"]["q"], "decisión abierta"


# --- Proceso 3 y 4: verificación ------------------------------------------------
def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    texto = {1: paginas(Path(sys.argv[1])), 2: paginas(Path(sys.argv[2]))}
    html = INDEX.read_text(encoding="utf-8")
    datos = json.loads(re.search(r'<script type="application/json" id="lb-data">(.*?)</script>', html, re.S).group(1))

    fallas = total = 0
    for tomo, pag, cita, lugar in citas(datos):
        total += 1
        q = normalizar(cita)
        p = pag + DESPLAZAMIENTO
        t = texto[tomo]
        if q in t.get(p, "") or q in t.get(p, "") + " " + t.get(p + 1, ""):
            continue
        fallas += 1
        donde = [k - DESPLAZAMIENTO for k, v in t.items() if q in v]
        print(f"FALLA [{lugar}] T{tomo} p.{pag}: encontrada en {donde or 'ninguna página'} :: {cita[:80]}")

    ids = {n["id"] for n in datos["nodes"]} | {p["id"] for p in datos["pols"]}
    rotos = [(e["from"], e["to"]) for e in datos["edges"] if e["from"] not in ids or e["to"] not in ids]
    rotos += [(p["id"], t["id"]) for p in datos["pols"] for t in p["targets"] if t["id"] not in ids]
    rotos += [(r["id"], i) for r in datos["tours"] for i in r["ids"] if i not in ids]

    print(f"Citas literales en su página: {total - fallas} de {total}")
    print(f"Referencias rotas: {rotos or 'ninguna'}")
    return 1 if fallas or rotos else 0


if __name__ == "__main__":
    sys.exit(main())
