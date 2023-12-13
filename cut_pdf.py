import PyPDF2

def reduce_pdf(input_file, output_file, num_pages):
    # Creating a pdf file reader object
    reader = PyPDF2.PdfReader(open(input_file, 'rb'))

    # Creating a pdf writer object
    writer = PyPDF2.PdfWriter()

    # Adding first num_pages pages to writer object
    for page_num in range(min(num_pages, len(reader.pages))):
        page = reader.pages[page_num]
        writer.add_page(page)

    # Writing out the pages to a new file
    with open(output_file, 'wb') as f:
        writer.write(f)

# Usage
reduce_pdf('AEJaspan-CV.pdf', 'output.pdf', 2)
