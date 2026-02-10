from fastapi import HTTPException
from app.schemas.items import ItemCreate, ItemUpdate

# Items "DB" List in memory
items_db: list[dict] = [] # consultar a chat
next_id: int = 1

# Look for existing Item in DB
def find_item_or_404(item_id: int) -> dict: # consultar chat
        for it in items_db:
             if it["id"] == item_id:
                  return it
        raise HTTPException(status_code=404, detail="Item not found")

# Create Item
def create_item_service(item: ItemCreate) -> dict:
    global next_id
    new_item = {"id": next_id, **item.model_dump()}
    items_db.append(new_item)
    next_id += 1
    return new_item

# List All Items
def list_items_service() -> list[dict]:
    return items_db

# Search an specific item
def get_item_service(item_id: int) -> dict:
     return find_item_or_404(item_id)

# Replace an existing Item for a NEW ONE
def update_item_service(item_id: int, item: ItemUpdate) -> dict:
     existing = find_item_or_404(item_id)
     existing.update(item.model_dump())
     return existing

# Delete an item from DB List
def delete_item_service(item_id: int) -> dict:
    item = find_item_or_404(item_id)
    items_db.remove(item)
    return {"deleted": True, "id": item_id}