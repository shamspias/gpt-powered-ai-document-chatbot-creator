# GPT Powered AI Document Chatbot Creator

GPT Powered AI Document Chatbot Creator is a web application that allows users to upload PDF and other document files, processes the documents' content, and provides answers to users' questions based on the information from the uploaded documents. The application uses OpenAI's GPT-3.5-turbo for processing questions and Text-Embedding-ADA-002 for embedding text, as well as Pinecone for vector similarity search.

## Overview
This project is designed to provide an easy-to-use interface for users to upload and manage their documents while getting accurate and relevant answers to their questions based on the content of the uploaded documents. The application leverages cutting-edge AI technology to provide a seamless and efficient user experience.

## Technology
- **Django**: The application is built using the Django web framework
- **Django Rest Framework**: API endpoints are created using Django Rest Framework
- **Celery**: Asynchronous task processing is handled using Celery
- **OpenAI API**: GPT-3.5-turbo is used for processing questions and generating standalone questions
- **Text-Embedding-ADA-002**: Text embeddings are created using OpenAI's text-embedding model
- **Pinecone**: Vector similarity search is performed using Pinecone.io
- **PostgresQL**: Default database for storing user and document information

## Features
- User authentication and management
- Document uploading and processing
- Text embedding and indexing in Pinecone
- Question processing using GPT-3.5-turbo
- Answer generation based on document similarity search
- Document management and organization

## Future Scope
- Support for additional document formats
- Enhanced document management and organization features
- Improved performance for processing large documents
- Integration with other AI models and services for improved answer generation
- Advanced analytics and reporting features for user insights
- Support for additional languages
- Support for additional question types

## Installation
- Clone the repository:
```bash
git clone https://github.com/shamspias/document_ai_qa.git
```
- Create a virtual environment and activate it:
```bash
cd document_ai_qa
python -m venv venv
source venv/bin/activate
```
- Install the required dependencies:
```bash
pip install -r requirements.txt
```
- Copy example.env to .env and update the environment variables:
```bash
cp example.env .env
```
```bash
# Django settings
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SETTINGS_MODULE=document_ai_qa.settings.local

# Database settings
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=db_host
DB_PORT=db_port

# OpenAI API
OPENAI_API_KEY=your-openai-api-key

# Pinecone API
PINECONE_API_KEY=your-pinecone-api-key

# Celery settings
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=''
EMAIL_PORT=587
EMAIL_FROM=""

SITE_URL=http://localhost:8000

# CORS
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_HTTPONLY=False
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE="None"
CSRF_COOKIE_SAMESITE="None"
CORS_ALLOW_CREDENTIALS=True
CORS_ORIGIN_ALLOW_ALL=False
CSRF_COOKIE_NAME="csrftoken"
CORS_ALLOWED_ORIGINS=http://127.0.0.1:3000,http://localhost:3000

# GENERALS
AUTH_USER_MODEL=users.User
LANGUAGE_CODE="en-us"
APPEND_SLASH=True
TIME_ZONE='UTC'
USE_I18N=True
USE_TZ=True
USE_L10N=True

# Social
FACEBOOK_KEY=''
FACEBOOK_SECRET=''
GOOGLE_KEY=''
GOOGLE_SECRET=''

# Other API
OPEN_AI_KEY=''
SENTRY_DSN=''

# AWS
AWS_ACCESS_KEY=''
AWS_SECRET_KEY=''
REGION_NAME=''
QUEUE_NAME=''

DJANGO_AWS_STORAGE_BUCKET_NAME=''


# Admin Site Config
ADMIN_SITE_HEADER="Chatbot builder"
ADMIN_SITE_TITLE="Chatbot Builder Dashboard"
ADMIN_SITE_INDEX="Chatbot Builder Dashboard"

```
- Apply the migrations:
```bash
python manage.py migrate
```
- Run the development server:
```bash
python manage.py runserver
```
Visit http://localhost:8000/ in your browser to access the application.


## API Endpoints

The following API endpoints are available in the GPT-Powered-AI-Document-Chatbot-Creator application:

1. User registration

    - Endpoint: `/api/auth/register/`
    - Method: `POST`
    - Payload: `{ "username": "your_username", "password": "your_password", "email": "your_email@example.com" }`
    - Description: Register a new user account.

2. User login

    - Endpoint: `/api/auth/login/`
    - Method: `POST`
    - Payload: `{ "username": "your_username", "password": "your_password" }`
    - Description: Authenticate an existing user and return a JSON Web Token (JWT).

3. Upload a document

    - Endpoint: `/api/documents/`
    - Method: `POST`
    - Payload: `{"title": "document_title", "file": file_upload}`
    - Description: Upload a document file (PDF or other supported formats) for processing and indexing.

4. List all documents

    - Endpoint: `/api/documents/`
    - Method: `GET`
    - Description: Retrieve a list of all uploaded documents for the authenticated user.
   
5. Retrieve a document

    - Endpoint: `/api/documents/<document_id>/`
    - Method: `GET`
    - Description: Retrieve a specific document by ID.

6. Delete a document

    - Endpoint: `/api/documents/<document_id>/`
    - Method: `DELETE`
    - Description: Delete a specific document by ID.
   
7. Ask a question

   - Endpoint: `/api/questions/`
   - Method: `POST`
   - Payload: `{ "question": "your_question" }`
   - Description: Submit a question and receive an answer based on the content of the uploaded documents.

Please note that the actual endpoints in your project might vary depending on the specific implementation. Refer to the project's source code and documentation for more detailed information on the available API endpoints and their usage.

## Usage
1. Register a new user account or log in with an existing account.
2. Upload PDF or other supported document files using the provided interface.
3. The application will process and index the content of the uploaded documents.
4. Ask questions using the question input field, and the application will provide answers based on the content of the uploaded documents. 

For more detailed usage instructions, please refer to the application's documentation.