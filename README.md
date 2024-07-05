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
    ```env
    SECRET_KEY=mysecret
    DATABASE_URL=postgresql://user:password@localhost/db_name
    JWT_SECRET_KEY=jwtsecret
    ```

4. Run the application:
    ```bash
    flask run
    ```

## API Endpoints

### Register a New User

- **URL**: `/register`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "username": "testuser",
        "password": "testpassword"
    }
    ```
- **Response**:
    ```json
    {
        "message": "User created successfully"
    }
    ```

### Login a User

- **URL**: `/login`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "username": "testuser",
        "password": "testpassword"
    }
    ```
- **Response**:
    ```json
    {
        "access_token": "your_jwt_token"
    }
    ```

### Send a Message to the Chatbot

- **URL**: `/chat`
- **Method**: `POST`
- **Headers**: 
    - `Authorization: Bearer your_jwt_token`
- **Request Body**:
    ```json
    {
        "message": "Hello"
    }
    ```
- **Response**:
    ```json
    {
        "response": "This is a mock response"
    }
    ```

### Get Conversation History

- **URL**: `/history`
- **Method**: `GET`
- **Headers**: 
    - `Authorization: Bearer your_jwt_token`
- **Response**:
    ```json
    {
        "history": [
            {
                "message": "Hello",
                "response": "This is a mock response",
                "timestamp": "2024-07-05T12:34:56"
            }
        ]
    }
    ```

## Deployment

### Docker

1. Build and run the Docker container:
    ```bash
    docker-compose up --build
    ```

2. Access the application at:
    ```
    http://localhost:5000
    ```

### Heroku

1. Log in to Heroku:
    ```bash
    heroku login
    ```

2. Create a new Heroku app:
    ```bash
    heroku create
    ```

3. Set up environment variables in Heroku:
    ```bash
    heroku config:set SECRET_KEY=mysecret
    heroku config:set DATABASE_URL=postgresql://user:password@localhost/db_name
    heroku config:set JWT_SECRET_KEY=jwtsecret
    ```

4. Deploy the application:
    ```bash
    git push heroku main
    ```

## Testing

1. Set up the testing environment and run tests:
    ```bash
    # Ensure the virtual environment is activated
    source venv/bin/activate

    # Run the tests
    python -m unittest discover -s tests
    ```

## CI/CD

### GitHub Actions

The project includes a GitHub Actions workflow for CI/CD located at `.github/workflows/ci.yml`. It runs tests and checks for each push and pull request to the `main` branch.

To set up CI/CD with GitHub Actions:

1. Ensure your repository is connected to GitHub.
2. GitHub Actions will automatically run the workflow on each push or pull request to the `main` branch.

## API Documentation

API documentation can be found in the `swagger.yaml` file. Import it into tools like Swagger UI or Postman for interactive API documentation.

## Postman Collection

You can use the provided `postman_collection.json` file to import the API endpoints into Postman and test them interactively.

## License

This project is licensed under the MIT License.
