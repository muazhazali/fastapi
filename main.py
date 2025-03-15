from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI(
    title="Demo FastAPI",
    description="A simple FastAPI application for teaching purposes",
    version="1.0.0"
)

# Pydantic model for request/response
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

# Basic GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World! Welcome to FastAPI"}

# Path parameter example
@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., description="The ID of the item to get", ge=1),
    q: Optional[str] = Query(None, description="Optional query parameter")
):
    return {"item_id": item_id, "query": q}

# POST endpoint with request body
@app.post("/items/")
def create_item(item: Item):
    return item

# PUT endpoint with path parameter and request body
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 