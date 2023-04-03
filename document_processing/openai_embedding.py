import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def embed_text(text):
    response = openai.Embedding.create(
        input="Your text string goes here",
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']
    return embeddings
