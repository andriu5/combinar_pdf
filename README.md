# combinar_pdf

Este script combina 2 archivos pdfs en un solo, uno de ellos esta completo y requiere remover e insertar una pagina de otro pdf.
## Requisitos

* Python 3.6 o superior
* Paquetes: os, argparse, datetime, PyPDF2

## Uso
Ejecutar el script con python y proporcionar los argumentos necesarios.

```py
python combinar_pdf.py --file1 archivo1.pdf --file2 archivo2.pdf --num_pagina 1 --nombre_pdf pdf_final
```

## Argumentos
`file1` : El primer archivo pdf de varias páginas.
`file2` : El segundo archivo pdf de una página a insertar.
`num_pagina` : El número de la página a remover e insertar del primer archivo pdf.
`nombre_pdf` : El nombre del pdf final.

## Funcionamiento

1. La función obtener_pdf(directorio) se utiliza para obtener todos los pdfs de un directorio.
2. La función insertar_pdf(pdf_paths, num_pagina, pdf_final) se encarga de remover la página especificada del primer archivo pdf e insertar la página del segundo archivo pdf en esa posición.
3. La función crear_pdf_final(nombre_pdf_salida) se utiliza para crear el nombre del pdf final y verificar que no exista.
4. La función nombre_pdf(nombre_pdf_salida) se utiliza para agregar la fecha y hora al nombre del pdf final.
5. El script se ejecuta con if __name__ == '__main__': y se leen los argumentos de la línea de comandos con parser.parse_args()

### Nota:
Es importante tener en cuenta que el número de la página a remover e insertar se refiere al número de página del archivo original, no del archivo final. Por lo tanto, si desea insertar una página en la posición 1, debe especificar 1 en el argumento num_pagina.
