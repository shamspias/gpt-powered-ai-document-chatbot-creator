from celery import shared_task
from .models import Document
from .utils import extract_text_from_file
import pinecone
import os
from openai_embedding import embed_text

pinecone.deinit()
pinecone.init(api_key=os.environ.get("PINECONE_API_KEY"))


@shared_task
def process_file(document_id, file, source_type):
    document = Document.objects.get(id=document_id)

    # Extract text from the file or URL
    extracted_text = extract_text_from_file(file, source_type)

    # Embed the text using Text-Embedding-ADA-002
    embedded_text = embed_text(extracted_text)

    # Save the embedded text to Pinecone
    pinecone_index_id = f"document-{document_id}"
    pinecone_index = pinecone.Index(index_name=pinecone_index_id)
    pinecone_index.upsert(1, [embedded_text])

    # Update the document with the Pinecone index ID
    document.pinecone_index_id = pinecone_index_id
    document.save()

    # Deinitialize Pinecone to release resources
    pinecone.deinit()
