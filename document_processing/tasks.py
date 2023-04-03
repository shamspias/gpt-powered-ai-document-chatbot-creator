from celery import shared_task
from django.contrib.auth.models import User
from .models import Document
from .utils import convert_pdf_to_text, scrape_website_text


@shared_task
def process_document(user_id, document_type, file=None, url=None):
    """
    Process the uploaded document (PDF or DOC) or URL and store the content in the Document model.
    """
    user = User.objects.get(id=user_id)

    if document_type in ['PDF', 'DOC']:
        content = convert_pdf_to_text(file)
    elif document_type == 'URL':
        content = scrape_website_text(url)
    else:
        raise ValueError("Invalid document type")

    document = Document(user=user, document_type=document_type, content=content)
    document.save()

    # Add the text embedding and Pinecone index ID logic here
    # document.pinecone_index_id = <your_pinecone_index_id>
    # document.save()

    return document.id
