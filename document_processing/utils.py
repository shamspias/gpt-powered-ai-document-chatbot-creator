import requests
from io import BytesIO
from PyPDF2 import PdfFileReader
import pandas as pd
from bs4 import BeautifulSoup


def get_source_type(file):
    extension = file.name.split('.')[-1].lower()
    return extension


def extract_text_from_file(file, source_type):
    """
    Extract text from a file or URL.
    :param file:  File or URL
    :param source_type: File type
    :return:  Extracted text
    """
    if source_type in ['pdf']:
        with open(file, 'rb') as f:
            reader = PdfFileReader(f)
            text = " ".join([reader.getPage(i).extractText() for i in range(reader.numPages)])
    elif source_type in ['csv', 'xls', 'xlsx']:
        df = pd.read_csv(file) if source_type == 'csv' else pd.read_excel(file)
        text = " ".join(df.to_string(index=False))
    elif source_type == 'json':
        df = pd.read_json(file)
        text = " ".join(df.to_string(index=False))
    elif source_type == 'url':
        response = requests.get(file)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
    else:
        raise ValueError('Unsupported source type')
    return text
