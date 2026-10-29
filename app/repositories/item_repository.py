from typing import Dict, List, Optional

from app.schemas.item import ItemCreate, ItemResponse


class ItemRepository:
    """Stores items in memory. A database repository can replace this later."""

    def __init__(self) -> None:
        self._items: Dict[int, ItemResponse] = {}
        self._next_id = 1

    def get_all(self) -> List[ItemResponse]:
        return list(self._items.values())

    def get_by_id(self, item_id: int) -> Optional[ItemResponse]:
        return self._items.get(item_id)

    def create(self, item: ItemCreate) -> ItemResponse:
        saved_item = ItemResponse(id=self._next_id, **item.dict())
        self._items[self._next_id] = saved_item
        self._next_id += 1
        return saved_item

    def update(self, item_id: int, item: ItemCreate) -> Optional[ItemResponse]:
        if item_id not in self._items:
            return None

        saved_item = ItemResponse(id=item_id, **item.dict())
        self._items[item_id] = saved_item
        return saved_item

    def delete(self, item_id: int) -> bool:
        if item_id not in self._items:
            return False

        del self._items[item_id]
        return True
