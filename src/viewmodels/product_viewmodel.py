from models.app import App_data
import os

class Product_viewmodel:
    def __init__(self, app_data : App_data):
        self.app_data = app_data
    pass

    def get_images(self, product_name : str):
        # Pega a partir do nome do produto o caminho da pasta do produto
        product_path = self.app_data.dict_products_path.get(product_name, "")
        num_images = self.app_data.dict_num_products_images.get(product_name, 0)

        # Lista de caminhos das imagens do produto
        images_paths = []
        
        # Adicionando imagens da pasta do produto à lista de caminhos das imagens
        for i in range(num_images):
            image_path = os.path.join(product_path, f"image_{i+1}.jpeg")
            print(f"Lendo imagem: {image_path}")

            images_paths.append(image_path)

        return images_paths
    pass
pass