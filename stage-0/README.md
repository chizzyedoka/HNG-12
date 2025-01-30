# FastAPI Project

## Description
This project is a simple FastAPI application that provides an endpoint to get user information, including the current datetime and a GitHub URL.

## Setup Instructions
To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone "https://github.com/chizzyedoka/HNG-12/tree/main/stage-0"
    cd "https://github.com/chizzyedoka/HNG-12/tree/main/stage-0"
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install fastapi uvicorn
    ```

4. Run the FastAPI application:
    ```sh
    uvicorn main:app --reload
    ```

5. Open your browser and navigate to `http://127.0.0.1:8000` to see the application running.

## API Documentation

### Endpoint
- **URL:** `/getUserInfo`
- **Method:** `GET`

### Request
No request parameters are required.

### Response
The response is a JSON object with the following structure:
```json
{
    "email": "chisomedoka48@gmail.com",
    "current_datetime": "2023-10-01T12:00:00Z",
    "github_url": "https://github.com/chizzyedoka/HNG-12"
}

This project is built using [Python](https://www.python.org/).