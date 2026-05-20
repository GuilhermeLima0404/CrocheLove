import flet as ft

class Product:
    def __init__(self, page : ft.Page, name : str):
        self.page = page
        self.name = name
        pass

    def build(self):
        return ft.Container(
            height=200,
            width=200,
            bgcolor=ft.Colors.PURPLE_400,
            content=ft.Column(
                controls=[
                    # Line 1
                    ft.Row(
                        expand=True,
                        controls=[
                            ft.Text(value=self.name),
                            ft.IconButton(icon=ft.Icons.REMOVE_CIRCLE),
                        ],
                    ),

                    # Line 2 - Image Slider

                ],
            )
        )
        pass
pass