# extract-PDF
Python script to extract and compile select page(s) from a single PDF file via command line.

## Extract page(s)
`python extract-pdf.py -i INPUT_FILE.pdf -p PAGE_NUMBER -o OUTPUT_FILE.pdf`.

**Options**

`-i` : PDF object to extract page(s) e.g. *INPUT_FILE.pdf*

`-p` : PDF page number(s) e.g. *1* *4* *3* 

`-o` : Name of output PDF file object that contains extracted pages e.g. *OUTPUT_FILE.pdf*