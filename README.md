# FastAPI Hello API

A simple FastAPI application with token authentication that returns a greeting message. The purpose of this repo is to be used for 
a Challenge. 

## Features

- Token-based authentication using an API key
- Environment variable configuration for token and message
- Docker and Docker Compose support
- Health check endpoint

## Environment Variables

The application uses two environment variables:

- `API_TOKEN`: A secret token that clients must provide for authentication
- `MESSAGE`: The greeting message to return (defaults to "World" if not provided)

## Running the Application

### Using Docker Compose

1. Clone this repository
2. (Optional) Edit the `docker-compose.yml` file to set your own `API_TOKEN` and `MESSAGE` values
3. Run the application:

```bash
docker-compose up -d
```

### Using Docker

```bash
# Build the Docker image
docker build -t fastapi-hello .

# Run the container
docker run -p 8000:8000 -e API_TOKEN=your_secret_token -e MESSAGE=YourName fastapi-hello
```

### Running Locally

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Set the environment variables:

```bash
export API_TOKEN=your_secret_token
export MESSAGE=YourName
```

3. Run the application:

```bash
uvicorn app:app --reload
```

## API Endpoints

- `GET /`: Returns a greeting message. Requires authentication.
- `GET /health`: Health check endpoint. Does not require authentication.

## API Authentication

To authenticate, include the API token in the `X-API-Key` header:

```
X-API-Key: your_secret_token
```

## Example Request

```bash
curl -X GET "http://localhost:8000/" -H "X-API-Key: your_secret_token_here"
```

Expected response:

```json
{"message": "Hello, FastAPI"}
``` 