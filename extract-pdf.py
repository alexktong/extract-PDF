import PyPDF2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', nargs='*', help='Input single PDF file to extract page(s)')
parser.add_argument('-p', '--page', nargs='*', help='Input PDF page number(s) to extract separated by space')
parser.add_argument('-o', '--output', nargs=1, help='Filename of extracted page(s)', required=True)

args = parser.parse_args()

option_input = args.input
option_page = args.page
option_output = args.output


def main():

    # read input file
    pdf_reader = PyPDF2.PdfFileReader(option_input[0])

    # create PDF writer object
    pdf_writer = PyPDF2.PdfFileWriter()

    # save select page numbers from input file
    for page in option_page:
        pdf_writer.addPage(pdf_reader.getPage(pageNumber=int(page)))

    # write saved pages into output
    with open(option_output[0], 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    main()