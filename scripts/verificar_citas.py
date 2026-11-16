"""Verifica que cada cita literal del mapa esté en la página que se indica.

Proceso:
  1. Extrae el texto de los cuatro documentos con pdftotext (Poppler), página por página.
  2. Recorre todo el JSON de index.html (bloque con id "lb-data") y reúne cada cita: todo objeto con
     tomo o documento ("t"), página impresa ("p") y texto literal ("q").
  3. Busca cada cita en su página (o en la siguiente, si cruza de una a otra).
  4. Revisa que flechas, respuestas, recorridos, hallazgos esenciales y bloques apunten a elementos que existen.

Uso:
  python scripts/verificar_citas.py libro_blanco_1.pdf libro_blanco_2.pdf estudio_oit.pdf marco_ocde.pdf

Documentos (no están en el repositorio):
  1 y 2  Libro Blanco, tomos 1 y 2 (EsSalud, 2019):
         https://www.essalud.gob.pe/transparencia/libro_blanco/libro_blanco_1.pdf (y _2.pdf)
  3      Valuación actuarial EsSalud al 2022 (OIT, 2023): https://www.social-protection.org/gimi/Media.action?id=20597
  4      Rethinking Health System Performance Assessment (OCDE, 2024): https://doi.org/10.1787/107182c8-en

Paquetes: solo la biblioteca estándar de Python (json, re, subprocess, pathlib, sys, tempfile).
Requiere el programa pdftotext en el PATH (viene con Poppler o con Git para Windows).
"""

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DESPLAZAMIENTO = {1: 2, 2: 2, 3: 0, 4: 2}  # página del PDF = página impresa + desplazamiento
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
    """Une palabras cortadas con guion al final de línea, colapsa espacios y unifica comillas."""
    texto = texto.replace("­", "")
    texto = re.sub(r"-\s*\n\s*", "", texto)
    texto = re.sub(r"\s+", " ", texto)
    texto = texto.replace("“", '"').replace("”", '"').replace("’", "'")
    return texto.strip().lower()


# --- Proceso 2: citas en cualquier lugar del JSON -------------------------------
def citas(obj, ruta="datos"):
    if isinstance(obj, dict):
        if {"t", "p", "q"} <= obj.keys():
            yield obj["t"], obj["p"], obj["q"], ruta
        for k, v in obj.items():
            yield from citas(v, f"{ruta}.{obj.get('id', k)}" if k == "quotes" else f"{ruta}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from citas(v, f"{ruta}[{i}]")


# --- Proceso 3 y 4: verificación ------------------------------------------------
def main() -> int:
    if len(sys.argv) != 5:
        print(__doc__)
        return 2
    texto = {i + 1: paginas(Path(a)) for i, a in enumerate(sys.argv[1:5])}
    html = INDEX.read_text(encoding="utf-8")
    bloque = re.search(r'<script type="application/json" id="lb-data">(.*?)</script>', html, re.S).group(1)
    datos = json.loads(bloque.replace("<\\/", "</"))

    fallas = total = 0
    for doc, pag, cita, lugar in citas(datos):
        total += 1
        q = normalizar(cita)
        p = pag + DESPLAZAMIENTO[doc]
        t = texto[doc]
        if q in t.get(p, "") or q in t.get(p, "") + " " + t.get(p + 1, ""):
            continue
        fallas += 1
        donde = [k - DESPLAZAMIENTO[doc] for k, v in t.items() if q in v]
        print(f"FALLA [{lugar}] doc {doc} p.{pag}: encontrada en {donde or 'ninguna página'} :: {cita[:80]}")

    ids = {n["id"] for n in datos["nodes"]}
    rotos = [(e["from"], e["to"]) for e in datos["edges"] if e["from"] not in ids or e["to"] not in ids]
    rotos += [(n["id"], t["id"]) for n in datos["nodes"] if n["col"] == "A" for t in n["targets"] if t["id"] not in ids]
    rotos += [(r["id"], i) for r in datos["tours"] for i in r["ids"] if i not in ids]
    rotos += [("esencial", i) for e in datos["essentials"] for i in e["ids"] if i not in ids]
    rotos += [(n["id"], n["blk"]) for n in datos["nodes"] if n["col"] != "A" and n["blk"] not in datos["blocks"]]

    print(f"Citas literales en su página: {total - fallas} de {total}")
    print(f"Referencias rotas: {rotos or 'ninguna'}")
    return 1 if fallas or rotos else 0


if __name__ == "__main__":
    sys.exit(main())
