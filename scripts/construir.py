"""Arma index.html a partir de la plantilla y los datos.

Proceso:
  1. Lee fuente/datos_mapa.json (nodos, flechas, recorridos) y fuente/datos_textos.json (textos, marcos, gráficos).
  2. Los une en un solo objeto JSON.
  3. Lo inserta en fuente/plantilla.html, en lugar de __DATOS__, y escribe index.html.

Uso:  python scripts/construir.py
Paquetes: solo la biblioteca estándar (json, pathlib).
"""

import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

mapa = json.loads((RAIZ / "fuente" / "datos_mapa.json").read_text(encoding="utf-8"))
textos = json.loads((RAIZ / "fuente" / "datos_textos.json").read_text(encoding="utf-8"))
datos = {**textos, **mapa}

# "</" se escapa para que el JSON no cierre la etiqueta <script> antes de tiempo.
bloque = json.dumps(datos, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
plantilla = (RAIZ / "fuente" / "plantilla.html").read_text(encoding="utf-8")
assert plantilla.count("__DATOS__") == 1
(RAIZ / "index.html").write_text(plantilla.replace("__DATOS__", bloque), encoding="utf-8", newline="\n")
print(f"index.html: {len(datos['nodes'])} nodos, {len(datos['edges'])} flechas, {len(bloque):,} caracteres de datos")
