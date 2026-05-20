import flet as ft
from routes.routes import HOME, LOGIN

class Home_view:
    def __init__(self, page : ft.Page):
        self.page = page
    pass

    async def go_to_login(self, e):
        await self.page.push_route(LOGIN)

    def build(self):
        return ft.View(
            route=HOME,
            appbar=ft.AppBar(
                title=ft.Text("HOME")
            ),
            controls=[
                ft.Text("Home Page"),
                ft.ElevatedButton(content=ft.Text(value="Go to Login"), on_click=self.go_to_login),
            ],
        )
pass