# Estudios sobre EsSalud-Perú

**Página:** https://diegosimemirror.github.io/libro_blanco/

EsSalud cumple dos oficios: como asegurador (IAFAS) afilia, recauda, guarda el fondo y paga la atención; como prestador (IPRESS) atiende en 389 establecimientos propios. Esta página ordena por rol lo que dicen dos estudios y lleva cada afirmación a su página en el PDF oficial:

- **Libro Blanco para el diálogo** (EsSalud, 2019). Tomo 1: 9 políticas y hoja de ruta 2019-2022. Tomo 2: estudios del Banco Mundial.
- **Valuación actuarial EsSalud al 2022** (OIT, 2023).

Dos interruptores marcan lo que respalda cada estudio. Así se ve dónde coinciden y qué trata cada uno: la OIT se concentra en el financiamiento del asegurador; el Libro Blanco, en la organización y la compra.

## Qué contiene

1. **Dos roles.** El asegurador según los procesos del DS 010-2016-SA y las funciones del financiamiento de la salud de la OMS. El prestador según el marco de evaluación del desempeño de la OCDE (2024). Cada bloque cuenta los hallazgos de cada estudio.
2. **Lo esencial.** Nueve hallazgos, tres por rol, con su cifra clave.
3. **Las cuentas.** Dos gráficos: ingresos y gastos 2009-2028 (Banco Mundial) y el crecimiento proyectado de ingresos y gastos en los dos estudios.
4. **El mapa.** 45 elementos en tres carriles (asegurador, prestador, gobierno) y cuatro columnas (causa, problema, efecto, respuesta), unidos por 48 relaciones. Puede mostrar solo lo esencial (20 elementos) y tiene cuatro recorridos con enlace propio (`#recorrido-dinero`, `#recorrido-paciente`, `#recorrido-compra`, `#recorrido-confianza`).
5. **Por qué no cambia.** Cuatro bucles de realimentación. Son una lectura propia (◇), con cada eslabón citado.
6. **Quién propone qué.** Quince temas, con lo que dice cada estudio y si coinciden.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `fuente/datos_mapa.json` | Elementos del mapa, citas, relaciones y recorridos. |
| `fuente/datos_textos.json` | Documentos, cifras, lo esencial, bloques de los marcos, datos de los gráficos, bucles y comparación. |
| `fuente/plantilla.html` | Diseño y código de la página. |
| `scripts/construir.py` | Une plantilla y datos en `index.html`. |
| `scripts/verificar_citas.py` | Comprueba que cada cita esté en su página y que no haya referencias rotas. |
| `index.html` | La página publicada (se genera; no se edita a mano). |

Para reconstruir y verificar:

```
python scripts/construir.py
python scripts/verificar_citas.py libro_blanco_1.pdf libro_blanco_2.pdf estudio_oit.pdf marco_ocde.pdf
```

Al publicar la versión 2, las 153 citas literales estaban en su página.

## Créditos, fuentes y derechos

Todas las publicaciones usadas son de acceso público y gratuito. Los enlaces llevan a las versiones que publican sus autores, a quienes corresponde el crédito por los datos, análisis y conclusiones citados. Esta página no ha sido revisada ni aprobada por EsSalud, el Banco Mundial, la OIT ni la OCDE.

Estudios analizados:

- EsSalud (2019). *Hacia la modernización de la seguridad social en el Perú. Libro blanco para el diálogo*, tomos [1](https://www.essalud.gob.pe/transparencia/libro_blanco/libro_blanco_1.pdf) y [2](https://www.essalud.gob.pe/transparencia/libro_blanco/libro_blanco_2.pdf). Derechos reservados de EsSalud: este repositorio no incluye los PDF ni su texto; la página cita fragmentos breves con fines de análisis.
  El tomo 2 reúne estudios elaborados por personal del Banco Mundial, con contribuciones externas, por encargo de EsSalud. También en el [repositorio institucional de EsSalud](https://repositorio.essalud.gob.pe/handle/20.500.12959/830).
- OIT (2023). *Valuación actuarial EsSalud. Estudio financiero actuarial al 2022*. Lima: OIT. Elaborado por los Servicios de Finanzas Públicas, Actuariales y Estadísticos de la OIT (Helmut Schwarzer, Cristina Lloret, Andrés Acuña y Sergio Velasco); redacción de Víctor Hugo Molinas; coordinación de Pablo Casalí. [PDF en la Plataforma de Protección Social de la OIT](https://www.social-protection.org/gimi/Media.action?id=20597). Licencia CC BY 4.0. Esta es una adaptación que no ha sido realizada, revisada ni aprobada por la OIT y no debe considerarse una adaptación oficial de la OIT.

Marcos conceptuales:

- OCDE (2024). *Rethinking Health System Performance Assessment: A Renewed Framework*. https://doi.org/10.1787/107182c8-en. Esta es una adaptación de un trabajo original de la OCDE; las opiniones expresadas no deben considerarse representativas de los puntos de vista oficiales de la OCDE o de sus países miembros.
- Kutzin, J., Witter, S., Jowett, M. y Bayarsaikhan, D. (2017). *Developing a national health financing strategy: a reference guide*. Health Financing Guidance n.º 3. Ginebra: OMS. [Sitio de la OMS](https://www.who.int/publications/i/item/9789241512107). Licencia CC BY-NC-SA 3.0 IGO.
- OIT (1952). *Convenio sobre la seguridad social (norma mínima)*, núm. 102. [NORMLEX](https://normlex.ilo.org/dyn/nrmlx_es/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C102).
- AISS. *Directrices de la AISS sobre buena gobernanza*. [Centro de conocimiento de la AISS](https://iskm.issa.int/node/5022).
- OISS (1995). *Código Iberoamericano de Seguridad Social*. Madrid. [Texto anexo a la Ley 516 de 1999 de Colombia (Colpensiones)](https://normativa.colpensiones.gov.co/colpensiones/docs/ley_0516_1999.htm).

El código (`fuente/plantilla.html`, `scripts/`) está bajo licencia MIT.

Análisis de Diego Sime, elaborado con Claude Code.
