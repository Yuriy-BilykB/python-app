from typing import List

from fastapi import APIRouter, HTTPException, Response, status

from app.schemas.item import ItemCreate, ItemResponse
from app.services.item_service import ItemNotFoundError, ItemService

router = APIRouter(prefix="/items", tags=["items"])
item_service = ItemService()


@router.get("", response_model=List[ItemResponse])
def read_items() -> List[ItemResponse]:
    return item_service.get_all_items()


@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int) -> ItemResponse:
    try:
        return item_service.get_item(item_id)
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="Item not found")


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate) -> ItemResponse:
    return item_service.create_item(item)


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate) -> ItemResponse:
    try:
        return item_service.update_item(item_id, item)
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> Response:
    try:
        item_service.delete_item(item_id)
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
