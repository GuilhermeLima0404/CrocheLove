# Dicionary que guarda as informações dos produtos, como nome e caminho da imagem

class App_data:
    def __init__(self):
        self.dict_products = {
            "Bolsa": "products_images/bolsa.png",
            "Pano de prato": "products_images/panodeprato.png",
            "Cachecol": "products_images/cachecol.png"
        }
        self.dict_routes = {
            "/": "Home_view",
        }
    pass