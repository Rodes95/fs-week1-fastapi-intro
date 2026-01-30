from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5173",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Item Model
class ItemCreate(BaseModel):
    title: str =  Field(..., min_length=2)
    description: Optional[str] = Field(default=None, max_length=200)

# Update Item Model
class ItemUpdate(BaseModel):
     title: str = Field(..., min_length=3)
     description: Optional[str] = Field(default=None, max_length=200)

# Items DB List
items_db = []
next_id = 1

# Look for existing Item in DB
def find_item_or_404(item_id: int):
        for it in items_db:
             if it["id"] == item_id:
                  return it
        raise HTTPException(status_code=404, detail="Item not found")

# Create Item
@app.post("/items")
def create_item(item: ItemCreate):
    global next_id
    new_item = {"id": next_id, **item.model_dump()}
    items_db.append(new_item)
    next_id += 1
    return new_item

# List All Items
@app.get("/items")
def list_items():
    return items_db

# Search an specific item
@app.get("/items/{item_id}")
def get_item(item_id: int):
     item = find_item_or_404(item_id)
     return item

# Replace an existing Item for a NEW ONE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
     existing = find_item_or_404(item_id)
     existing.update(item.model_dump())
     return existing

# Delete an item from DB List
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item = find_item_or_404(item_id)
    items_db.remove(item)
    return {"deleted": True, "id": item_id}

# Main Page
@app.get("/")
def root():
    return {"message: Hello, Ro"}

# Check Page Status
@app.get("/health")
def health():
    return {"status: ok"}