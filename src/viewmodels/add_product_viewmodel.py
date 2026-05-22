import shutil
import os
from models.app import App_data
from services.database_manager import save_product

class Add_product_viewmodel:
    def __init__(self, app_data : App_data):
        self.app_data = app_data
        pass

    def add_product(self, name: str, files):

        folder_path = f"src/assets/products_images/{name}_images"
        os.makedirs(folder_path, exist_ok=True)

        if not files:
            print("Nenhum arquivo recebido", flush=True)
            return

        print(f"Recebido {len(files)} arquivos para o produto '{name}'", flush=True)

        for i, file in enumerate(files):
            extension = os.path.splitext(file.name)[1]

            new_name = f"image_{i+1}{extension}"
            destination = os.path.join(folder_path, new_name)

            print(f"Salvando: {file.name} -> {destination}", flush=True)

            shutil.copy(file.path, destination)

        # Salvar o caminho da imagem no banco de dados
        save_product(name=name, path=folder_path, route=f"/{name}", app=self.app_data)
pass