from fastapi import FastAPI

from app.api.routes.items import router as items_router

app = FastAPI(title="Beginner CRUD API")

# Add the item routes to the main FastAPI application.
app.include_router(items_router)


@app.get("/")
def read_home() -> dict:
    return {"message": "Welcome! Try /items or open /docs."}
