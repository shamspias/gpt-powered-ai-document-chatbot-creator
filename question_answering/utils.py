from .models import Conversation


def fetch_answer_from_gpt3(question, context):
    """
    Fetch the answer from the GPT-3 model using the given question and context.
    """
    # Replace this with your actual GPT-3 API call
    answer = f"Sample answer for question '{question}' in context '{context}'"
    return answer


def save_conversation(chatbot, user, text, response):
    """
    Save the conversation between the user and the chatbot.
    """
    conversation = Conversation(chatbot=chatbot, user=user, text=text, response=response)
    conversation.save()
