# Mapa del Libro Blanco de EsSalud

**Página:** https://diegosimemirror.github.io/libro_blanco/

El *Libro Blanco para el diálogo. Hacia la modernización de la seguridad social en el Perú* (EsSalud, 2019) tiene dos tomos y unas 590 páginas. El tomo 1 plantea 9 políticas y una hoja de ruta 2019-2022. El tomo 2 reúne los estudios que EsSalud encargó al Banco Mundial. Pocos tomadores de decisiones lo leen completo.

Esta página lo convierte en un mapa de trazabilidad. Muestra qué causas de fondo identifica el libro, qué problemas producen, qué efectos tienen sobre los asegurados y la institución, y qué política propone para cada uno. Cada afirmación lleva su página, y al pulsarla se abre el PDF oficial de EsSalud en esa página.

## Qué contiene

- **La tesis en cinco frases**, cada una con su cita.
- **EsSalud dentro del sistema de salud**: un diagrama con los actores que fijan sus ingresos, sus reglas y su competencia (Congreso, MTPE, Fonafe, Minsa, Susalud, Sunat, otros seguros, prestadores externos y asegurados).
- **Mapa de trazabilidad**: 11 causas raíz (2 son presiones del entorno), 9 problemas, 8 efectos y las 9 políticas, unidos por 41 relaciones causales. Tiene cuatro recorridos guiados: el dinero, el paciente, la compra y la confianza.
- **Seis bucles de realimentación** que explican por qué el problema persiste. Son una lectura propia (marcada con ◇), con cada eslabón sostenido por una cita.
- **Las 9 políticas**, con sus estrategias, los hitos de la hoja de ruta y lo que agrega el tomo 2.
- **Lo que el libro deja abierto**: seis decisiones sin cerrar y cinco recomendaciones del tomo 2 que no pasaron a la hoja de ruta del tomo 1.

## Cómo se hizo

1. Se extrajo el texto de los dos PDF con `pdftotext`. El tomo 1 se leyó completo. Del tomo 2 se leyeron completos los resúmenes, diagnósticos, conclusiones y recomendaciones de los ocho estudios; el detalle técnico se consultó por búsqueda.
2. Cada elemento se clasificó como causa, problema, efecto o respuesta siguiendo la teoría del cambio del propio libro (tomo 1, p. 17). La clasificación es propia.
3. Las 116 citas literales se verificaron por programa contra el texto de la página citada.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La página completa: estilos, datos (bloque JSON `lb-data`) y código, sin dependencias externas salvo Google Fonts. |
| `scripts/verificar_citas.py` | Comprueba que cada cita esté en la página indicada y que no haya referencias rotas. |

Para verificar las citas, descargue los dos PDF de EsSalud y ejecute:

```
python scripts/verificar_citas.py libro_blanco_1.pdf libro_blanco_2.pdf
```

## Fuente y derechos

EsSalud (2019). *Hacia la modernización de la seguridad social en el Perú. Libro blanco para el diálogo.* Tomo 1: Políticas y hoja de ruta para el fortalecimiento del Seguro Social de Salud, EsSalud 2019-2022. Tomo 2: Compendio de estudios. Lima: EsSalud.

- Tomo 1: https://www.essalud.gob.pe/transparencia/libro_blanco/libro_blanco_1.pdf
- Tomo 2: https://www.essalud.gob.pe/transparencia/libro_blanco/libro_blanco_2.pdf
- Repositorio institucional: https://repositorio.essalud.gob.pe/handle/20.500.12959/830

El libro tiene derechos reservados de EsSalud. Este repositorio no incluye los PDF ni su texto; la página cita fragmentos breves con fines de análisis, siempre con su fuente. El código (`index.html` y `scripts/`) está bajo licencia MIT.

Análisis de Diego Sime, elaborado con Claude Code.
