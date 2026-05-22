import flet as ft
from routes.routes import HOME, ADMIN
from models.product import Product
from viewmodels.home_viewmodel import Home_viewmodel

class Home_view:
    def __init__(self, page : ft.Page, vm : Home_viewmodel):
        self.page = page
        self.vm = vm
    pass
    
    async def go_to_adm_view(self, e):
        await self.page.push_route(ADMIN)
    
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
                            on_click=self.go_to_adm_view,
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
                        Product(self.page, name, path, adm_mode=False).build()
                        for name, path in self.page.data.dict_products_path.items()
                    ],
                )
            ],
        )
pass