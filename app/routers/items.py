from fastapi import APIRouter
from app.schemas.items import ItemCreate, ItemUpdate
from app.services.items import (
    create_item_service,
    list_items_service,
    get_item_service,
    update_item_service,
    delete_item_service,
)

# Group endpoints
# prefix means that all routes start with /items. "/" --> "/items"
# tags just groups endpoints in /docs
router = APIRouter(prefix="/items", tags=["items"])

@router.post("", status_code=200)
def create_item(item: ItemCreate): # The JSON data will be checked by ItemCreate...
    return create_item_service(item)

@router.get("")
def list_items():
    return list_items_service()

@router.get("/{item_id}")
def get_item(item_id: int):
    return get_item_service(item_id)

@router.put("/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    return update_item_service(item_id, item)

@router.delete("/{item_id}")
def delete_item(item_id: int):
    return delete_item_service(item_id)