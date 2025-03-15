# FastAPI Demo Application

This is a simple FastAPI application created for teaching purposes. It demonstrates basic FastAPI features including:
- Path parameters
- Query parameters
- Request body validation
- Pydantic models
- API documentation

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```
or
```bash
uvicorn main:app --reload
```

The application will start on `http://localhost:8000`

## Available Endpoints

- `GET /`: Returns a welcome message
- `GET /items/{item_id}`: Get an item by ID (with optional query parameter 'q')
- `POST /items/`: Create a new item
- `PUT /items/{item_id}`: Update an existing item

## API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Request Body (for POST and PUT)

```json
{
    "name": "Example Item",
    "price": 9.99,
    "is_offer": true
}
``` 