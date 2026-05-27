from unicodedata import name

import flet as ft
from routes.routes import HOME, ADMIN, ADD_PRODUCT, REFRESH
from models.product import Product
from viewmodels.adm_viewmodel import Adm_viewmodel


class Adm_view:
    def __init__(self, page : ft.Page, vm : Adm_viewmodel):
        self.page = page
        self.vm = vm
    pass

    async def remove_product(self, name):
        print(f"Remover produto: {name}")
        self.vm.remove_product(name)
        await self.page.push_route(REFRESH)
    pass

    async def go_to_add_product(self):
        await self.page.push_route(ADD_PRODUCT)
    pass

    def build(self):
        return ft.View(
            route=ADMIN,
            scroll=ft.ScrollMode.AUTO,
            bgcolor=ft.Colors.WHITE,
            appbar=ft.AppBar(
                title=ft.Stack(
                    height=60,
                    controls=[
                        ft.Container(
                            alignment=ft.Alignment.CENTER_LEFT,
                            content=ft.Image(
                                src="crochelovelogo_horiz.png",
                                height=50,
                                fit=ft.BoxFit.CONTAIN,
                            ),
                        ),

                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text(
                                value="Área do Administrador, salve novos produtos e gerencie os existentes.",
                                font_family="Montserrat",
                                size=30,
                                color=ft.Colors.BLACK,
                            ),
                        ),
                    ],
                ),
            ),
            controls=[
                ft.GridView(
                    expand=True,
                    max_extent=300,  # tamanho de cada card
                    spacing=10,
                    run_spacing=10,
                    controls=[
                        # Grid View dos produtos
                        Product(self.page, name, path, adm_mode=True, delete_callback=self.remove_product).build()
                        for name, path in self.page.data.dict_products_path.items()
                    ]
                    +
                    [
                        # Container adicionar produto
                        ft.Container(
                            height=300,
                            width=300,
                            bgcolor=self.page.theme.color_scheme.primary_container,
                            border_radius=10,
                            shadow=ft.BoxShadow(
                                blur_radius=25,
                                color=ft.Colors.BLACK_38,
                                offset=ft.Offset(0, 8),
                            ),
                            content=ft.IconButton(
                                icon=ft.Icons.ADD,
                                icon_size=50,
                                on_click=self.go_to_add_product,
                            )
                        ),
                    ],
                )
            ],
        )
pass