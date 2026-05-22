from models.app import App_data
from services.database_manager import delete_product


class Adm_viewmodel:
    def __init__(self, app_data : App_data):
        self.app_data = app_data

    def remove_product(self, name):
        delete_product(name, self.app_data)
    pass
pass