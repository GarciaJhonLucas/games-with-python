import pandas as pd
import pdfquery

#read the PDF
pdf = pdfquery.PDFQuery('customers.pdf')
pdf.load()

#convert the pdf to XML
pdf.tree.write('customers.xml', pretty_print = True)

# access the data using coordinates
customer_name = pdf.pq('example")').text()
print(customer_name)