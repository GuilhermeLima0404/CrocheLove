import flet as ft
from routes.routes import LOGIN

class Login_view:
    def __init__(self, page : ft.Page):
        self.page = page
    pass

    def build(self):
        return ft.View(
            route=LOGIN,
            appbar=ft.AppBar(
                title=ft.Text(value="LOGIN")
            ),
            controls=[
                ft.Text(value="Login Page")
            ],
        )
pass