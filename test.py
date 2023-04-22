from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

items = {
    1: {"name": "Item 1", "description": "This is item 1"},
    2: {"name": "Item 2", "description": "This is item 2"},
    3: {"name": "Item 3", "description": "This is item 3"},
}

@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str, description: str):
    items[item_id]["name"] = name
    items[item_id]["description"] = description
    return {"message": f"Item {item_id} updated successfully"}

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

@app.get("/items/{item_id}")
async def edit_item(request: Request, item_id: int):
    item = items[item_id]
    return templates.TemplateResponse("edit_item.html", {"request": request, "item": item})