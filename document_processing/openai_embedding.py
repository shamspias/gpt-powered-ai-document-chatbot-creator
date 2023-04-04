from langchain.embeddings import OpenAIEmbeddings
from django.conf import settings


def embed_text(text):
    embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
    doc_result = embeddings.embed_documents([text])
    return doc_result

# def embed_text(text):
#     response = openai.Embedding.create(
#         input=text,
#         model="text-embedding-ada-002"
#     )
#     embeddings = response['data'][0]['embedding']
#     return embeddings
