from pydantic import BaseModel, Field
from typing import Optional

# Create Item Model
class ItemCreate (BaseModel):
    title: str = Field(..., min_length=2)
    description: Optional[str] = Field(default=None, max_length=200)

# Update Item Model
class ItemUpdate(BaseModel):
    title: str = Field(..., min_length=3)
    description: Optional[str] = Field(default=None, max_length=200)
