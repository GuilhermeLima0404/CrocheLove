import flet as ft
from routes.routes import ADMIN
from models.product import Product
from viewmodels.adm_viewmodel import Adm_viewmodel

class Adm_view:
    def __init__(self, page : ft.Page, vm : Adm_viewmodel):
        self.page = page
        self.vm = vm
    pass

    def build(self):
        return ft.View(
            route=ADMIN,
            scroll=ft.ScrollMode.AUTO,
            bgcolor=ft.Colors.WHITE,
            appbar=ft.AppBar(
                bgcolor="#4cc9f0",
                elevation=0,
                title=ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    controls=[
                        ft.Image(
                            align=ft.Alignment.CENTER_LEFT,
                            src="crochelovelogo_horiz.png",
                            height=50,  
                            fit=ft.BoxFit.CONTAIN,
                        ),                        
                        ft.Text(
                            value="Área do administrador",
                            text_align=ft.Alignment.CENTER_RIGHT,
                            size=40,
                            color=ft.Colors.BLACK,
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
                        # Grid View dos produtos
                        Product(self.page, name, path).build()
                        for name, path in self.page.data.dict_products.items()
                    ]
                    +
                    [
                        # Container adicionar produto
                        ft.Container(
                            height=300,
                            width=300,
                            bgcolor="#8c53b3",
                            border_radius=10,
                            shadow=ft.BoxShadow(
                                blur_radius=25,
                                color=ft.Colors.BLACK_38,
                                offset=ft.Offset(0, 8),
                            ),
                            content=ft.IconButton(
                                icon=ft.Icons.ADD,
                                on_click=self.vm.add_product,
                            )
                        ),
                    ],
                )
            ],
        )
pass