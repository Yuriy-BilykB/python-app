from pydantic import BaseModel


class ItemCreate(BaseModel):
    """Fields a client must send when creating or replacing an item."""

    name: str
    description: str = ""
    price: float


class ItemResponse(ItemCreate):
    """Fields the API returns, including the server-assigned ID."""

    id: int
