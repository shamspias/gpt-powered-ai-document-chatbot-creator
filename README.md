# Document AI Question Answering

Document AI Question Answering is a web application that allows users to upload PDF and other document files, processes the documents' content, and provides answers to users' questions based on the information from the uploaded documents. The application uses OpenAI's GPT-3.5-turbo for processing questions and Text-Embedding-ADA-002 for embedding text, as well as Pinecone for vector similarity search.

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
- Apply the migrations:
```bash
python manage.py migrate
```
- Run the development server:
```bash
python manage.py runserver
```
Visit http://localhost:8000/ in your browser to access the application.

## Usage
1. Register a new user account or log in with an existing account.
2. Upload PDF or other supported document files using the provided interface.
3. The application will process and index the content of the uploaded documents.
4. Ask questions using the question input field, and the application will provide answers based on the content of the uploaded documents. 

For more detailed usage instructions, please refer to the application's documentation.