import flet as ft
from routes.routes import HOME, LOGIN
from models.product import Product

class Home_view:
    def __init__(self, page : ft.Page):
        self.page = page
    pass
    
    #async def go_to_login(self, e):
    #    await self.page.push_route(LOGIN)
    
    def build(self):
        return ft.View(
            route=HOME,
            appbar=ft.AppBar(
                title=ft.Row(
                    controls=[
                        ft.Text("Loja Croche Love", align=ft.Alignment.CENTER_LEFT),
                        ft.Button(
                            content=ft.Text(value="Area Adiministrador"),
                            align=ft.Alignment.CENTER_RIGHT,
                        ),
                        ft.Image(src="assets/icon.png", width=100, height=100),
                    ],
                )
                
            ),
            controls=[
                ft.Text("Catálogo de produtos", align=ft.Alignment.TOP_CENTER, size=50),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                Product(self.page, "Cachecol").build()
                            ]
                        ),
                        ft.Row(
                            controls=[
                                Product(self.page, "Bolsa").build()
                            ]
                        ),
                        ft.Row(
                            controls=[
                                Product(self.page, "Pano de prato").build()
                            ]
                        )
                    ]
                )
            ],
        )
pass