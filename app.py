"""A tiny in-memory CRUD API for learning Python and FastAPI.

Run it with: uvicorn app:app --reload
Then open:   http://127.0.0.1:8000/docs
"""

from typing import Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# BaseModel describes the shape of data that clients send to our API.
class Item(BaseModel):
    name: str
    description: str = ""
    price: float


# FastAPI uses this object to register routes and generate API documentation.
app = FastAPI(title="Beginner CRUD API")

# This dictionary is our temporary data store. The integer is the item's ID.
# Data disappears when the server stops; later we can replace this with a database.
items: Dict[int, Item] = {}
next_item_id = 1


@app.get("/")
def read_home() -> dict:
    """A small welcome route so we know the server is running."""
    return {"message": "Welcome! Try /items or open /docs."}


# READ: return every item.
@app.get("/items", response_model=List[Item])
def read_items() -> List[Item]:
    return list(items.values())


# READ: return one item, selected by its ID in the URL.
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int) -> Item:
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# CREATE: accept an item in the request body and assign it a new ID.
@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item) -> Item:
    global next_item_id

    items[next_item_id] = item
    next_item_id += 1
    return item


# UPDATE: replace all editable fields on an existing item.
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    items[item_id] = updated_item
    return updated_item


# DELETE: remove an item. A successful delete has no response body (204).
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    del items[item_id]
