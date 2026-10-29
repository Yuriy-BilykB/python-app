from typing import List

from app.repositories.item_repository import ItemRepository
from app.schemas.item import ItemCreate, ItemResponse


class ItemNotFoundError(Exception):
    """Raised when an operation refers to an item that does not exist."""


class ItemService:
    """Coordinates item operations and turns missing records into clear errors."""

    def __init__(self, repository: ItemRepository = None) -> None:
        self._repository = repository or ItemRepository()

    def get_all_items(self) -> List[ItemResponse]:
        return self._repository.get_all()

    def get_item(self, item_id: int) -> ItemResponse:
        item = self._repository.get_by_id(item_id)
        if item is None:
            raise ItemNotFoundError
        return item

    def create_item(self, item: ItemCreate) -> ItemResponse:
        return self._repository.create(item)

    def update_item(self, item_id: int, item: ItemCreate) -> ItemResponse:
        saved_item = self._repository.update(item_id, item)
        if saved_item is None:
            raise ItemNotFoundError
        return saved_item

    def delete_item(self, item_id: int) -> None:
        if not self._repository.delete(item_id):
            raise ItemNotFoundError
