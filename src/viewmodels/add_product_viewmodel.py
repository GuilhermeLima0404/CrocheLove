import shutil
import os

from models.app import App_data
from services.database_manager import save_product

class Add_product_viewmodel:
    def __init__(self, app_data: App_data):
        self.app_data = app_data

    def add_product(self, name: str, files=None):
        # Criar pasta do produto
        folder_path = f"src/assets/products_images/{name}_images"
        os.makedirs(folder_path, exist_ok=True)

        upload_folder = "src/assets/uploads"

        if files is not None:
            for i, file in enumerate(files):
                # Pega apenas o nome do arquivo
                filename = os.path.basename(file.name)

                source_path = os.path.join(upload_folder, filename)

                destination_path = os.path.join(folder_path, filename)

                print(source_path)
                print(destination_path)

                shutil.move(source_path, destination_path)

                print(
                    f"Arquivo {source_path} movido para {destination_path}",
                    flush=True
                )

                # Renomeando 
                extension = os.path.splitext(file.name)[1]
                new_name = f"image_{i+1}{extension}"
                os.rename(destination_path, os.path.join(folder_path, new_name))
        else:   
            print("Nenhum arquivo selecionado para upload.")

        save_product(
            name=name,
            path=f"products_images/{name}_images",
            route=f"/{name}",
            app=self.app_data
        )