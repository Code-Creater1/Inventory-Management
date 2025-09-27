import json
import os

INVENTORY_FILE = "inventory.json"

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_inventory(data):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_inventory():
    return load_inventory()

def add_item(item):
    inventory = load_inventory()
    if item.name in inventory:
        inventory[item.name]['quantity'] += item.quantity
    else:
        inventory[item.name] = {
            "quantity": item.quantity,
            "price": item.price
        }
    save_inventory(inventory)

def update_item(name, updates):
    inventory = load_inventory()
    if name in inventory:
        if updates.quantity is not None:
            inventory[name]['quantity'] = updates.quantity
        if updates.price is not None:
            inventory[name]['price'] = updates.price
        save_inventory(inventory)
        return True
    return False

def delete_item(name):
    inventory = load_inventory()
    if name in inventory:
        del inventory[name]
        save_inventory(inventory)
        return True
    return False
