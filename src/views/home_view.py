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
            scroll=ft.ScrollMode.AUTO,
            bgcolor=ft.Colors.WHITE,
            appbar=ft.AppBar(
                bgcolor="#4cc9f0",
                elevation=0,
                title=ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Image(
                            align=ft.Alignment.CENTER,
                            src="crochelovelogo_horiz.png",
                            height=50,  
                            fit=ft.BoxFit.CONTAIN,
                        ),                        
                        ft.Button(
                            content=ft.Text(value="Adiministrador"),
                            align=ft.Alignment.CENTER,
                        ),
                    ],
                )
            ),
            controls=[
                ft.Column(
                    expand=True,
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                Product(self.page, "Pano de cozinha").build(),
                                Product(self.page, "Cachecol").build(),
                                Product(self.page, "Cachecol").build(),
                                Product(self.page, "Cachecol").build(),
                                Product(self.page, "Cachecol").build(),
                            ]
                        ),
                        ft.Row(
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                Product(self.page, "Bolsa").build(),
                                Product(self.page, "Saia de praia").build(),
                                Product(self.page, "Cachecol").build(),
                                Product(self.page, "Cachecol").build(),
                                Product(self.page, "Rede pet").build(),
                            ]
                        ),
                        ft.Row(
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                Product(self.page, "Pano de prato").build(),
                                Product(self.page, "Cachecol").build(),
                                Product(self.page, "Cachecol").build(),
                                Product(self.page, "Kit amor de mãe").build(),
                                Product(self.page, "Cachecol").build(),
                            ]
                        )
                    ]
                )
            ],
        )
pass