import flet as ft

class Product:
    def __init__(self, page : ft.Page, name : str, path : str, adm_mode : bool = False, delete_callback = None):
        self.page = page
        self.name = name
        self.path = path
        self.adm_mode = adm_mode
        self.delete_callback = delete_callback
        pass
    
    async def handle_delete(self):
        if self.delete_callback and self.adm_mode:
            await self.delete_callback(self.name)

    def build(self):
        return ft.Stack(
            width=300,
            height=300,
            controls=[
                # Card principal
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
                    content=ft.Column(
                        controls=[
                            # Linha 1 - Imagem
                            ft.Container(
                                height=200,
                                width=300,
                                content=ft.Image(
                                    src=f"{self.path}/image_1.png",
                                    fit=ft.BoxFit.FIT_WIDTH,
                                ),
                            ),

                            # Linha 2 - Nome do produto
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
                    ),
                ),

                # Botão deletar produto (apenas em modo admin)
                ft.Container(
                    top=5,
                    right=5,
                    content=ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.RED,
                        on_click=self.handle_delete,
                        hover_color=ft.Colors.RED_300,
                    ),
                ) if self.adm_mode else ft.Container(),
            ],
        )
    pass
pass