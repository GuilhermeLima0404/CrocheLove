import os
import shutil

from models.app import App_data
import json

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # src/
_DB_PATH = os.path.join(_BASE_DIR, "database", "database.json")
_ASSETS_PATH = os.path.join(_BASE_DIR, "assets", "products_images")

# SAVE
def save_product(name : str, num_images : int, path : str, route:str, app : App_data):
    app.dict_products_path[name] = path
    app.dict_routes[name] = route
    app.dict_num_products_images[name] = num_images

    data = {
        "dict_products_path": app.dict_products_path,
        "dict_routes": app.dict_routes,
        "dict_num_products_images": app.dict_num_products_images
    }

    try:
        with open(_DB_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("Product saved successfully.")
        
        return True
    except Exception as e:
        print("Error saving product:", e)
        return False

# GET
def get_product_image_path(name : str, app : App_data):
    return app.dict_products_path.get(name)

def get_product_route(name : str, app : App_data):
    return app.dict_routes.get(name)

def get_prouct_name_list(app : App_data):
    return list(app.dict_routes.keys())

def get_app_data():
    try:
        with open(_DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        app_data = App_data()
        app_data.dict_products_path = data.get("dict_products_path", {})
        app_data.dict_routes = data.get("dict_routes", {})
        app_data.dict_num_products_images = data.get("dict_num_products_images", {})

        print(app_data.dict_products_path)
        print(app_data.dict_routes)
        print(app_data.dict_num_products_images)
        print("App data loaded successfully.")

        return app_data

    except FileNotFoundError:
        print("Database file not found. Returning empty app data.")
        return App_data()

# UPDATE
def update_dict_routes(dict_new : dict):
    pass

# DELETE
def delete_product(name : str, app : App_data):
    shutil.rmtree(os.path.join(_ASSETS_PATH, f"{name}_images"), ignore_errors=True)

    if name in app.dict_products_path:
        del app.dict_products_path[name]

    if name in app.dict_routes:
        del app.dict_routes[name]

    if name in app.dict_num_products_images:
        del app.dict_num_products_images[name]

    data = {
        "dict_products_path": app.dict_products_path,
        "dict_routes": app.dict_routes,
        "dict_num_products_images": app.dict_num_products_images
    }

    try:
        with open(_DB_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("Product deleted successfully.")
        
        return True
    except Exception as e:
        print("Error deleting product:", e)
        return False
