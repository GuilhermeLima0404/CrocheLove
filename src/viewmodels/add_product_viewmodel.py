import os
import shutil

from models.app import App_data
from services.database_manager import get_prouct_name_list, save_product

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # src/
_PRODUCTS_IMAGES_DIR = os.path.join(_BASE_DIR, "assets", "products_images")
_UPLOAD_DIR = os.path.join(_BASE_DIR, "assets", "uploads")

class Add_product_viewmodel:
    def __init__(self, app_data: App_data):
        self.app_data = app_data

    def add_product_web(self, name: str, files=None):
        folder_path = os.path.join(_PRODUCTS_IMAGES_DIR, f"{name}_images")
        os.makedirs(folder_path, exist_ok=True)

        if files is not None:
            for i, file in enumerate(files):
                filename = os.path.basename(file.name)
                source_path = os.path.join(_UPLOAD_DIR, filename)
                destination_path = os.path.join(folder_path, filename)

                print(source_path)
                print(destination_path)

                shutil.move(source_path, destination_path)

                print(f"Arquivo {source_path} movido para {destination_path}", flush=True)

                extension = os.path.splitext(file.name)[1]
                new_name = f"image_{i+1}{extension}"
                os.rename(destination_path, os.path.join(folder_path, new_name))
        else:
            print("Nenhum arquivo selecionado para upload.")

        save_product(
            name=name,
            num_images=len(files),
            path=f"products_images/{name}_images",
            route=f"/{name}",
            app=self.app_data
        )

    def add_product_desktop(self, name: str, files):
        folder_path = os.path.join(_PRODUCTS_IMAGES_DIR, f"{name}_images")
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

        save_product(
            name=name,
            num_images=len(files),
            path=f"products_images/{name}_images",
            route=f"/{name}",
            app=self.app_data
        )

    def get_product_names(self):
        return get_prouct_name_list(self.app_data)
