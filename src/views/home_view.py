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
                ft.GridView(
                    expand=True,
                    max_extent=300,  # tamanho de cada card
                    spacing=10,
                    run_spacing=10,
                    controls=[
                        Product(self.page, name, path).build()
                        for name, path in self.page.data.dict_products.items()
                    ],
                )
            ],
        )
pass