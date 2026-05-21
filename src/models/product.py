import flet as ft

class Product:
    def __init__(self, page : ft.Page, name : str):
        self.page = page
        self.name = name
        pass

    def build(self):
        return ft.Container(
            height=300,
            width=200,
            bgcolor="#8c53b3",
            border_radius=10,
            shadow=ft.BoxShadow(
                blur_radius=25,
                color=ft.Colors.BLACK_38,
                offset=ft.Offset(0, 8),
            ),
            content=ft.Column(
                controls=[
                    # Line 1 - Image
                    ft.Container(
                        height=200,
                        width=200,
                        content=ft.Image(
                            src="products_images/bolsa.png",
                            height=200,
                            fit=ft.BoxFit.COVER,
                        ), 
                    ),                 

                    # Line 2 - Nome do produto
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[
                            ft.Text(
                                value=self.name,
                                font_family="Tangerine",
                                width=200,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                size=40,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                    ),
                ],
            )
        )
        pass
pass