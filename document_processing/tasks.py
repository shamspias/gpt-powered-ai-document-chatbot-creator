# tasks.py
from django.conf import settings
import pinecone
from celery import shared_task
from .utils import extract_text_from_file
from .openai_embedding import embed_text

# Initialize Pinecone
pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT)

# Get a list of Pinecone indexes
active_indexes = pinecone.list_indexes()

# Check if the Pinecone index exists
index_exists = settings.PINECONE_INDEX_NAME in active_indexes

# Create the Pinecone index if it doesn't exist
if not index_exists:
    pinecone.create_index(name=settings.PINECONE_INDEX_NAME, dimension=1536, metric="cosine")


@shared_task
def process_file(document_id, file, source_type):
    """
    Process a file and add it to the Pinecone index
    :param document_id:
    :param file:
    :param source_type:
    :return:
    """
    text = extract_text_from_file(file, source_type)
    embedded_text = embed_text(text)

    with pinecone.Index(index_name=settings.PINECONE_INDEX_NAME) as index:
        index.upsert(items={str(document_id): embedded_text})

    return "Successfully processed and saved the document."
