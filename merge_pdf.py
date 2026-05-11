"""CLI script to concatenate PDF files in order. Based on pdf_merging.py from combinar_pdf repo."""
import argparse
import sys
from datetime import datetime
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(input_paths: list[str], output: str) -> None:
    writer = PdfWriter()
    for path in input_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)
    print(f"PDF combinado guardado en: {output}")


def build_output_name(first_input: str) -> str:
    stem = Path(first_input).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return str(Path(first_input).parent / f"{stem}_combinado_{timestamp}.pdf")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Concatena múltiples archivos PDF en uno solo.\n"
            "Ejemplo: python merge_pdf.py archivo1.pdf archivo2.pdf\n"
            "         python merge_pdf.py archivo1.pdf archivo2.pdf --output resultado.pdf"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        metavar="PDF",
        help="Archivos PDF a concatenar, en orden.",
    )
    parser.add_argument(
        "--output", "-o",
        metavar="SALIDA",
        default=None,
        help="Nombre del PDF de salida (opcional). Si se omite se genera automáticamente.",
    )
    args = parser.parse_args()

    missing = [p for p in args.inputs if not Path(p).is_file()]
    if missing:
        for m in missing:
            print(f"ERROR: Archivo no encontrado: {m}", file=sys.stderr)
        sys.exit(1)

    output_path = args.output if args.output else build_output_name(args.inputs[0])
    merge_pdfs(args.inputs, output_path)
