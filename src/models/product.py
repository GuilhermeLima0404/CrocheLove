import flet as ft

class Product:
    def __init__(self, page : ft.Page, name : str, path : str, adm_mode : bool = False, delete_callback = None):
        self.page = page
        self.name = name
        self.path = path
        self.adm_mode = adm_mode
        self.delete_callback = delete_callback
        pass
    
    async def handle_delete(self, e):
        if self.delete_callback and self.adm_mode:
            await self.delete_callback(self.name)

    async def product_details(self, e):
        print(f"Produto clicado: {self.name}")
        await self.page.push_route(f"/Produto/{self.name}")

    # Animações
    def hover_animation(self, e : ft.HoverEvent):
        if e.data == True:
            # Mouse entrou
            e.control.offset = ft.Offset(0, -0.03)
            e.control.scale = 1.03

            e.control.shadow = ft.BoxShadow(
                blur_radius=40,
                color=ft.Colors.BLACK_45,
                offset=ft.Offset(0, 15),
            )

        else:
            # Mouse saiu
            e.control.offset = ft.Offset(0, 0)
            e.control.scale = 1

            e.control.shadow = ft.BoxShadow(
                blur_radius=25,
                color=ft.Colors.BLACK_38,
                offset=ft.Offset(0, 8),
            )

        e.control.update()

    def build(self):
        return ft.Stack(
            data=self.name,
            controls=[
                # Card principal
                ft.Container(
                    border_radius=10,

                    on_click=self.product_details,
                    on_hover=self.hover_animation,

                    animate_offset=300,
                    animate_scale=300,

                    bgcolor=self.page.theme.color_scheme.primary_container,
                    shadow=ft.BoxShadow(
                        blur_radius=25,
                        color=ft.Colors.BLACK_38,
                        offset=ft.Offset(0, 8),
                    ),
                    content=ft.Column(
                        #tight=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            # Linha 1 - Imagem
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        expand=True,
                                        aspect_ratio=1.4,
                                        content=ft.Image(
                                            src=f"{self.path}/image_1.jpeg",
                                            fit=ft.BoxFit.COVER,
                                        ),
                                    ),
                                ]
                            ),

                            # Linha 2 - Nome do produto
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        value=self.name,
                                        font_family="Tangerine-Bold",
                                        max_lines=1,
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                        size=40 if self.page.width >= 800 else 20,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
            ] 
            + # Botão deletar produto (apenas em modo admin)
            (
                [
                    ft.Container(
                        top=5,
                        right=5,
                        content=ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.RED,
                            on_click=self.handle_delete,
                        ),
                    )
                ] if self.adm_mode else []
            )
        )
    pass
pass