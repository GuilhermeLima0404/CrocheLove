import shutil

from models.app import App_data
import json

# SAVE
def save_product(name : str, path : str, route:str, app : App_data):
    app.dict_products_path[name] = path
    app.dict_routes[name] = route

    # Salvar o dicionário atualizado no arquivo "database.json", usando JSON
    data = {
        "dict_products_path": app.dict_products_path,
        "dict_routes": app.dict_routes
    }

    try:
        with open("src/database/database.json", "w", encoding="utf-8") as f:
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

def get_app_data():
    # Ler o arquivo "database.json" e retornar os dicionários de produtos e rotas
    try:
        with open("src/database/database.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        app_data = App_data()
        app_data.dict_products_path = data.get("dict_products_path", {})
        app_data.dict_routes = data.get("dict_routes", {})

        print(app_data.dict_products_path)
        print(app_data.dict_routes)

        print("App data loaded successfully.")

        return app_data

    except FileNotFoundError:
        print("Database file not found. Returning empty app data.")
        return App_data()
    
# UPDATE
def update_dict_routes(dict_new : dict):

    # Atualizar o dicionário de rotas associadas a View no arquivo "dict_routes.py"
    pass

# DELETE
def delete_product(name : str, app : App_data):
    # Deletar a pasta de imagens do produto
    shutil.rmtree(f"src/assets/products_images/{name}_images", ignore_errors=True)

    # Remover o caminho das imagens do produto do dicionário
    if name in app.dict_products_path:
        del app.dict_products_path[name]

    # Remover a rota da view do produto do dicionario
    if name in app.dict_routes:
        del app.dict_routes[name]

    # Salvar as alterações no arquivo "database.json"
    data = {
        "dict_products_path": app.dict_products_path,
        "dict_routes": app.dict_routes
    }

    try:
        with open("src/database/database.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("Product deleted successfully.")
        
        return True
    except Exception as e:
        print("Error deleting product:", e)
        return False