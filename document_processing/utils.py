import PyPDF2


def convert_pdf_to_text(file_path):
    """
    Convert a PDF file to text.
    :param file_path: Path to the PDF file
    :return:  Text extracted from the PDF file
    """
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text


def scrape_website_text(url):
    """
    Scrape text from a given website URL.
    """
    # Replace this with your actual web scraping logic
    return "Sample text scraped from the website"
