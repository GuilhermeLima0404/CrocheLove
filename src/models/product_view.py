import flet as ft
from models.product import Product

class Product_view:
    def __init__(self, product : Product, page : ft.Page):
        self.product = product
        self.page = page
        pass

    def build(self):
        return ft.View(
            route= f"/{self.product.name}",
            scroll=ft.ScrollMode.AUTO,
            bgcolor=ft.Colors.WHITE,
            appbar=ft.AppBar(
                bgcolor="#8c53b3",
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
                        ft.Text(
                            value=self.product.name,
                            size=40,
                        ),
                    ],
                )
            ),
        )
        
        
pass