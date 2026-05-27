from models.app import App_data


class Home_viewmodel:
    def __init__(self, app_data : App_data):
        self.app_data = app_data
    pass

    def validate_password(self, password : str) -> bool:
        # Aqui você pode implementar a lógica de validação da senha
        # Por exemplo, comparar com uma senha pré-definida ou verificar em um banco de dados
        return True if password == "raqueladmin123" else False
pass