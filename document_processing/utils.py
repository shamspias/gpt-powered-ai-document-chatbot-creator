from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import (
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader,
    UnstructuredURLLoader,
)


def get_source_type(file):
    if file.name.startswith('https://youtube.com', 'https://www.youtube.com', 'www.youtube.com', 'youtube.com'):
        return 'youtube'
    elif file.name.startswith('http', 'https', 'www.'):
        return 'url'
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
        loader = PyPDFLoader(file_path=file)
        pages = loader.load_and_split()
        list_text = pages

    elif source_type in ['csv', 'xls', 'xlsx']:
        loader = CSVLoader(file_path=file)
        data = loader.load()
        list_text = data

    elif source_type == 'docx':
        loader = UnstructuredWordDocumentLoader(file_path=file)
        data = loader.load()
        list_text = data

    elif source_type == 'pptx':
        loader = UnstructuredPowerPointLoader(file_path=file)
        data = loader.load()
        list_text = data

    elif source_type in ['jpg', 'png', 'jpeg']:
        loader = UnstructuredPowerPointLoader(file_path=file)
        data = loader.load()
        list_text = data

    elif source_type == 'url':
        loader = UnstructuredPowerPointLoader(file_path=file)
        data = loader.load()
        list_text = data

    elif source_type == 'website':
        loader = UnstructuredPowerPointLoader(file_path=file)
        data = loader.load()
        list_text = data

    elif source_type == 'youtube':
        loader = UnstructuredPowerPointLoader(file_path=file)
        data = loader.load()
        list_text = data
    else:
        raise ValueError('Unsupported source type')
    return list_text
