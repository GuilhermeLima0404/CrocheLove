import flet as ft

from routes.routes import ADD_PRODUCT, ADMIN
from viewmodels.add_product_viewmodel import Add_product_viewmodel

class Add_product_view:
    def __init__(self, page: ft.Page, vm: Add_product_viewmodel):
        self.page = page
        self.vm = vm

        # Widgets
        self.files = None
        self.selected_files = ft.Text(color=ft.Colors.BLACK, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS)
        self.product_name_field = ft.TextField(expand=True, label="Nome do produto", color=ft.Colors.BLACK, border_color=ft.Colors.BLACK, label_style=ft.TextStyle(color=ft.Colors.BLACK),)
    pass

    async def handle_save(self):
        await self.save_product(self.product_name_field.value, self.files)
    pass

    async def save_product(self, name: str, files):
        self.vm.add_product(name, files)

        # Voltando para a tela admin
        await self.page.push_route(ADMIN)
    pass

    async def handle_pick_files(self, e: ft.Event[ft.Button]):
        self.files = await ft.FilePicker().pick_files(allow_multiple=True)
        self.selected_files.value = (
            ", ".join(map(lambda f: f.name, self.files)) if self.files else "Cancelled!"
        )
    pass

    def build(self):
        return ft.View(
            route=ADD_PRODUCT,
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
                            value="Adicionar novo produto",
                            text_align=ft.Alignment.CENTER_RIGHT,
                            size=40,
                            color=ft.Colors.BLACK,
                        ),
                    ],
                ),
            ),
            controls=[
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Container(
                        width=600,
                        height=800,
                        bgcolor="#4cc9f0",
                        border_radius=10,
                        shadow=ft.BoxShadow(
                            blur_radius=25,
                            color=ft.Colors.BLACK_38,
                            offset=ft.Offset(0, 8),
                        ),
                        content=ft.Column(
                            margin=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                self.product_name_field,                # Campo de nome do produto
                                ft.ElevatedButton(                      # Botão para escolher arquivos
                                    "Pick files",
                                    icon=ft.Icons.UPLOAD_FILE,
                                    on_click=self.handle_pick_files,
                                ),
                                self.selected_files,                    # Texto para mostrar os arquivos selecionados
                                ft.Row(                 
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.IconButton(                  # Botão para salvar o produto
                                            bgcolor=ft.Colors.GREEN,
                                            expand=True,
                                            icon=ft.Icons.ADD,
                                            on_click=self.handle_save,
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ),
                )
            ],
        )
