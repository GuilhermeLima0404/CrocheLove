import shutil
import os

class Add_product_viewmodel:
    def __init__(self):
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
pass