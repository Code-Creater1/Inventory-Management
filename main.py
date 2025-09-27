from fastapi import FastAPI, HTTPException
from models import Item, UpdateItem
import storage

app = FastAPI(title="Inventory Management API")

@app.get("/")
def root():
    return {"message": "Inventory API is running"}

@app.get("/items")
def list_items():
    return storage.get_inventory()

@app.post("/items")
def create_item(item: Item):
    storage.add_item(item)
    return {"message": f"Item '{item.name}' added/updated successfully."}

@app.put("/items/{name}")
def update_item(name: str, updates: UpdateItem):
    success = storage.update_item(name, updates)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Item '{name}' updated."}

@app.delete("/items/{name}")
def delete_item(name: str):
    success = storage.delete_item(name)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": f"Item '{name}' deleted."}
