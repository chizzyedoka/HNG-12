# Number Properties API

A FastAPI-based REST API that analyzes numbers and returns their mathematical properties along with interesting facts.

## Features

- Analyzes input numbers for various mathematical properties
- Integrates with Numbers API for mathematical fun facts
- Returns comprehensive JSON responses with number properties
- Input validation and error handling
- RESTful architecture

## Mathematical Properties Analyzed

- Armstrong numbers
- Prime numbers
- Perfect numbers
- Parity (odd/even)
- Digit sum
- Mathematical fun facts

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd number-properties-api
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install fastapi uvicorn requests
```

## Running the Application

1. Start the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

2. Alternative method using uvicorn directly:
```bash
uvicorn main:app --reload
```

## API Documentation

### Endpoint

`GET /api/classify-number`

### Query Parameters

- `number` (required): Integer to analyze

### Success Response Format

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response Format

```json
{
    "number": "alphabet",
    "error": true
}
```

### Properties Combinations

The `properties` field in the response can have the following combinations:
1. `["armstrong", "odd"]` - for Armstrong numbers that are odd
2. `["armstrong", "even"]` - for Armstrong numbers that are even
3. `["odd"]` - for non-Armstrong odd numbers
4. `["even"]` - for non-Armstrong even numbers

## Examples

1. Get properties of number 371:
```bash
curl "http://localhost:8000/api/classify-number?number=371"
```

2. Invalid input example:
```bash
curl "http://localhost:8000/api/classify-number?number=abc"
```

## Error Handling

- Returns 400 Bad Request for invalid inputs
- Returns appropriate error messages in JSON format
- Handles missing parameters and invalid number formats

## Dependencies

- FastAPI: Modern web framework for building APIs
- Uvicorn: ASGI server implementation
- Requests: HTTP library for Python
- Pydantic: Data validation using Python type annotations

## Development

The application structure is modular and follows best practices:
- Input validation using Pydantic models
- Separation of concerns with distinct f