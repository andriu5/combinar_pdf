# combinar_pdf

Colección de scripts Python para manipular y combinar archivos PDF.

## Requisitos

* Python 3.6 o superior
* Paquetes: `PyPDF2`, `argparse`, `datetime`

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Scripts

### `merge_pdf.py` — Concatenar múltiples PDFs

Concatena dos o más archivos PDF en uno solo, en el orden en que se indican. Si no se especifica nombre de salida, lo genera automáticamente usando el nombre del primer archivo más una marca de tiempo.

#### Uso

```bash
# Dos archivos
python merge_pdf.py archivo1.pdf archivo2.pdf

# Nombre de salida personalizado
python merge_pdf.py archivo1.pdf archivo2.pdf --output resultado.pdf

# Tres o más archivos
python merge_pdf.py a.pdf b.pdf c.pdf -o combinado.pdf
```

#### Argumentos

| Argumento | Descripción |
|---|---|
| `PDF` (posicional) | Uno o más archivos PDF a concatenar, en orden. |
| `--output`, `-o` | Nombre del archivo PDF de salida (opcional). Si se omite, se genera automáticamente como `<primer_archivo>_combinado_<timestamp>.pdf`. |

---

### `pdf_merging.py` — Módulo base de fusión

Módulo de utilidad que expone la función `merge_pdfs()`. No cuenta con interfaz de línea de comandos; está pensado para ser importado desde otros scripts.

```python
from pdf_merging import merge_pdfs

merge_pdfs(['archivo1.pdf', 'archivo2.pdf'], output='merged.pdf')
```

---

### `combinar_pdf.py` — Reemplazar una página de un PDF

Combina 2 archivos PDF en uno solo: toma el primer PDF completo, elimina una página específica e inserta en su lugar la página del segundo PDF.

#### Uso

```bash
python combinar_pdf.py --file1 archivo1.pdf --file2 archivo2.pdf --num_pagina 1 --nombre_pdf pdf_final
```

#### Argumentos

| Argumento | Descripción |
|---|---|
| `--file1` | El primer archivo PDF de varias páginas. |
| `--file2` | El segundo archivo PDF (una página a insertar). |
| `--num_pagina` | Número de página a remover del primer PDF e insertar la del segundo. |
| `--nombre_pdf` | Nombre base del PDF final (se añade fecha y hora automáticamente). |

#### Funcionamiento

1. `obtener_pdf(directorio)` — obtiene todos los PDFs de un directorio.
2. `insertar_pdf(pdf_paths, num_pagina, pdf_final)` — elimina la página indicada del primer PDF e inserta la página del segundo en esa posición.
3. `crear_pdf_final(nombre_pdf_salida)` — construye el nombre del archivo de salida verificando que no exista.
4. `nombre_pdf(nombre_pdf_salida)` — agrega fecha y hora al nombre del PDF final.

> **Nota:** `--num_pagina` hace referencia al número de página en el archivo original, no en el resultado final. Para insertar en la primera posición, use `--num_pagina 1`.
