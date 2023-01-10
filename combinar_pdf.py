"""Este script combina 2 archivos pdfs en un solo, uno de ellos esta completo y requiere remover e insertar una pagina de otro pdf."""
import os
import argparse
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter


# escrbir una funcion que obtenga todos los pdfs de un directorio
def obtener_pdf(directorio):
    pdfs = []
    for archivo in os.listdir(directorio):
        if archivo.endswith('.pdf'):
            pdfs.append(archivo)
    pdfs.sort(key=str.lower)
    return pdfs

# escribir una funcion que remueva pagina e inserte un pdf en la pagina especificada
def insertar_pdf(pdf_paths, num_pagina, pdf_final):

    pdf_writer = PdfWriter()

    pdf_reader1 = PdfReader(pdf_paths[0])
    pdf_reader2 = PdfReader(pdf_paths[1])
    for pagina in range(len(pdf_reader1.pages)):
        # remover pagina
        if pagina != num_pagina:
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader1.pages[pagina])
        else:
            # insertar pdf desde pagina especificada
            pdf_writer.add_page(pdf_reader2.pages[0])    

    # Write out the merged PDF
    with open(pdf_final, 'wb') as out:
        pdf_writer.write(out)

# crear pdf final y verificar que no exista
def crear_pdf_final(nombre_pdf_salida):
    try:
        # crear pdf final usando nombre_pdf
        nombre_archivo = nombre_pdf(nombre_pdf_salida)
        print('El nombre del archivo se creo correctamente')
    except:
        print('El nombre del archivo ya existe')
    else:
        return nombre_archivo


def nombre_pdf(nombre_pdf_salida):
    # agregar fecha y hora al nombre del pdf
    nombre_archivo = '{}_{}.pdf'.format(nombre_pdf_salida,datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
    return nombre_archivo

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Este script sirve para unir pdfs: \
        uno de ellos es un PDF de varias páginas, mientras que el segundo es de una \
        página. Ejemplo: python combinar_pdf.py --file1 archivo1.pdf \
        --file2 archivo2.pdf --num_pagina 1 --nombre_pdf pdf_final')
    # Ejemplo de ejecucion:
    # python combinar_pdf.py --file1 "archivo1.pdf" --file2 "archivo2.pdf" --num_pagina 24 --nombre_pdf pdf_final_
    parser.add_argument('--file1', help='archivo pdf de varias paginas')
    parser.add_argument('--file2', help='archivo pdf de una pagina a insertar')
    parser.add_argument('--num_pagina', help='numero de pagina a remover e insertar')
    parser.add_argument('--nombre_pdf', help='nombre del pdf final')
    argumentos = parser.parse_args()

    # leer argumentos de la linea de comandos
    num_pagina = int(argumentos.num_pagina)-1 if int(argumentos.num_pagina)-1 > 0 else 0
    pdf_final = crear_pdf_final(argumentos.nombre_pdf)
    pdfs = [argumentos.file1, argumentos.file2]

    # insertar pdf
    insertar_pdf(pdfs, num_pagina, pdf_final)

