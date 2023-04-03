import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Util:

    @staticmethod
    def send_email(data):
        """
        Sends an email using the provided data.

        Args:
            data (dict): A dictionary containing the email data including:
                - subject: The email subject
                - message: The plain text email content
                - html_message: The HTML email content
                - from_email: The sender's email address
                - recipient_list: A list of recipient email addresses

        Returns:
            None
        """

        email = EmailMultiAlternatives(
            subject=data['subject'],
            body=data['message'],
            from_email=data['from_email'],
            to=data['recipient_list']
        )

        if 'html_message' in data:
            email.attach_alternative(data['html_message'], "text/html")

        email.send()

    @staticmethod
    def send_email_sendgrid(data):
        """
        Sends an email using SendGrid with the provided data.

        Args:
            data (dict): A dictionary containing the email data including:
                - subject: The email subject
                - html_content: The HTML email content
                - from_email: The sender's email address
                - to_emails: A list of recipient email addresses

        Returns:
            None
        """

        message = Mail(
            from_email=data['from_email'],
            to_emails=data['to_emails'],
            subject=data['subject'],
            html_content=data['html_content']
        )

        try:
            sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sendgrid_client.send(message)
        except Exception as e:
            print(e)


def render_email_template(template_name, context):
    """
    Renders an email template with the given context.

    Args:
        template_name (str): The name of the template file
        context (dict): A dictionary containing context data for the template

    Returns:
        str: The rendered HTML content of the template
    """

    return render_to_string(template_name, context)
