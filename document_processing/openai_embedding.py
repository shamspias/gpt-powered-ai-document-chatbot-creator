import openai
from django.conf import settings

openai.api_key = settings.OPEN_AI_KEY


def embed_text(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']
    return embeddings
