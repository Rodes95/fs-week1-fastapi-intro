from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class ItemCreate(BaseModel):
    title: str =  Field(..., min_length=2)
    description: Optional[str] = Field(default=None, max_length=200)

items_db = []
next_id = 1

@app.post("/items")
def create_item(item: ItemCreate):
    global next_id
    new_item = {"id": next_id, **item.model_dump()}
    items_db.append(new_item)
    next_id += 1
    return new_item

@app.get("/items")
def list_items():
    return items_db

@app.get("/")
def root():
    return {"message: Hello, Ro"}

@app.get("/health")
def health():
    return {"status: ok"}