import PyPDF2

def merge_pdfs(filepaths, output_path):
    pdf_writer = PyPDF2.PdfFileWriter()

    for filepath in filepaths:
        pdf_reader = PyPDF2.PdfFileReader(filepath)
        for page_num in range(len(pdf_reader.numPages)):
            pdf_writer.addPage(pdf_reader.pages(page_num))

    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

# Example usage
filepaths = ['Unit 1 - Machine Learning - www.rgpvnotes.in', 'Unit 2 - Machine Learning - www.rgpvnotes.in','Unit 3 - Machine Learning - www.rgpvnotes.in','Unit 4 - Machine Learning - www.rgpvnotes.in','Unit 5 - Machine Learning - www.rgpvnotes.in']  # List of PDF file paths to merge
output_path = 'ml.pdf'  # Output file path

merge_pdfs(filepaths, output_path)
