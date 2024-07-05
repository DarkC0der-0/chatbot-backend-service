# Chatbot Backend Service

This project is a Flask-based backend service that integrates natural language processing (NLP) for chatbot functionality. It includes user authentication, conversation history, and deployment using Docker and Heroku.

## Features

- User authentication
- Natural language processing (NLP)
- Conversation history
- Docker support
- CI/CD with GitHub Actions

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/chatbot-backend-service.git
    cd chatbot-backend-service
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up environment variables in a `.env` file:
    ```bash
    SECRET_KEY=mysecret
    DATABASE_URL=postgresql://user:password@localhost/db_name
    JWT_SECRET_KEY=jwtsecret
    ```

4. Run the application:
    ```bash
    flask run
    ```

## Usage

### Register

- **URL**: `/register`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "password": "testpassword"
  }

