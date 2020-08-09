from fastapi import FastAPI
from starlette.responses import RedirectResponse
from os import environ

ENV = environ["ENV"]


def app_kwargs():
    if ENV in ("test", "prod"):
        return dict(root_path=f"/{ENV}")
    else:
        return dict()


def root_path():
    if ENV in ("test", "prod"):
        return f"/{ENV}"
    else:
        return ""


app = FastAPI(**app_kwargs())


@app.post("/api/items/")
def create_item(item_id: int):
    return {"id": item_id}


@app.get("/api/items/")
def list_items():
    items = [{"id": i} for i in range(10)]
    return items


@app.get("/")
def read_root():
    return RedirectResponse(f"{root_path()}/redoc")

