---
applyTo: "**/*.py"
---

# PDF Manipulation — combinar_pdf repo

This repo contains three Python scripts for manipulating and combining PDF files using **PyPDF2**. Always prefer the existing scripts over writing new PDF logic from scratch.

## Available scripts

### `merge_pdf.py` — Concatenate any number of PDFs (CLI)

Use this when the task is to **join two or more PDFs in sequence** without removing or replacing any pages.

```bash
# Two files, auto-generated output name
python merge_pdf.py archivo1.pdf archivo2.pdf

# Custom output name
python merge_pdf.py archivo1.pdf archivo2.pdf --output resultado.pdf

# Three or more files
python merge_pdf.py a.pdf b.pdf c.pdf -o combinado.pdf
```

Key implementation details:
- Uses `PdfReader` / `PdfWriter` from `PyPDF2`.
- If `--output` / `-o` is omitted, output is named `<first_stem>_combinado_<YYYYMMDD_HHMMSS>.pdf` next to the first input.
- Validates that all input files exist before merging; exits with code 1 and a clear error message otherwise.

### `pdf_merging.py` — Core merge utility (importable module)

Use this when another script needs to **merge PDFs programmatically** (not via CLI).

```python
from pdf_merging import merge_pdfs

merge_pdfs(['archivo1.pdf', 'archivo2.pdf', 'archivo3.pdf'], output='merged.pdf')
```

`merge_pdfs(paths: list, output: str)` iterates over every page of every path in order and writes the result to `output`.

### `combinar_pdf.py` — Replace one page of a PDF with a page from another (CLI)

Use this when the task is to **swap/replace a specific page** of a multi-page PDF with the single page from a second PDF.

```bash
python combinar_pdf.py --file1 archivo1.pdf --file2 archivo2.pdf --num_pagina 1 --nombre_pdf pdf_final
```

Arguments:
- `--file1` — multi-page base PDF.
- `--file2` — single-page PDF whose page replaces the removed page.
- `--num_pagina` — 1-based page number in `file1` to replace.
- `--nombre_pdf` — output base name; a `DD-MM-YYYY_HH-MM-SS` timestamp is appended automatically.

Important: Internally the script converts `--num_pagina` to a 0-based index (`int(num_pagina) - 1`, floored at 0). Keep this in mind if extending the logic.

## Dependency

All scripts depend on **PyPDF2** (pinned to `3.0.1` in `requirements.txt`).

```bash
pip install -r requirements.txt
```

Do not introduce other PDF libraries (e.g. `pdfplumber`, `pypdf`, `reportlab`) unless the existing ones cannot satisfy the requirement.

## Conventions

- Output files always end in `.pdf`.
- When generating output names automatically, append a timestamp to avoid collisions.
- Page numbers exposed to the user are **1-based**; convert to 0-based internally.
- Print a confirmation message to stdout after writing a PDF (e.g. `PDF combinado guardado en: <path>`).
- Validate inputs (file existence, argument types) before any write operation.
