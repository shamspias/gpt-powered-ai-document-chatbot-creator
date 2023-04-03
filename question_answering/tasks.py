from celery import shared_task
from .models import Chatbot, Conversation
from .utils import fetch_answer_from_gpt3, save_conversation


@shared_task
def ask_chatbot(chatbot_id, user_id, text):
    """
    Ask the chatbot a question and store the response in the conversation history.
    """
    chatbot = Chatbot.objects.get(id=chatbot_id)
    user = User.objects.get(id=user_id)
    context = chatbot.get_context()  # Implement the get_context method in the Chatbot model
    response = fetch_answer_from_gpt3(text, context)
    save_conversation(chatbot, user, text, response)
    return response
