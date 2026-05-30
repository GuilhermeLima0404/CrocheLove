import os
import flet as ft

from viewmodels.product_viewmodel import Product_viewmodel

class Product_view:
    def __init__(self, name : str, path : str, page : ft.Page, vm : Product_viewmodel):
        self.name = name
        self.path = path
        self.page = page
        self.vm = vm

        self.images_list = self.get_images(name)
        self.current_image_index = 0

        # Widgets
        self.right_arrow = ft.IconButton(
            icon=ft.Icons.ARROW_CIRCLE_RIGHT_OUTLINED, 
            on_click=self.go_right, 
            on_hover=self.on_hover_arrow, 
            bgcolor=ft.Colors.TRANSPARENT, 
            icon_color=ft.Colors.WHITE,
            height=100,
            width=100,
            icon_size=50,
        )

        self.left_arrow = ft.IconButton(
            icon=ft.Icons.ARROW_CIRCLE_LEFT_OUTLINED, 
            on_click=self.go_left, 
            on_hover=self.on_hover_arrow, 
            bgcolor=ft.Colors.TRANSPARENT, 
            icon_color=ft.Colors.WHITE,
            height=100,
            width=100,
            icon_size=50,
        )

        self.switcher = ft.AnimatedSwitcher(
            content = self.images_list[0],
            duration=500,
            reverse_duration=500,
        )

        self.copy_button = ft.ElevatedButton(
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            content=ft.Row(
                controls=[
                    ft.Icon(
                        icon=ft.Icons.COPY,
                        size=20,
                    ),
                    ft.Text(
                        value="Copiar Número",
                        font_family="Montserrat",
                    ),
                ]
            ),
            on_click=self.set_to_clipboard
        )

        self.number_text = ft.TextField(
            value="51 8150-2727",
            read_only=True,
            text_align=ft.TextAlign.CENTER,
            text_size=20,
            border_color=ft.Colors.WHITE,
            width=250,
            color=ft.Colors.WHITE,
        )
    
    # Arrows functions
    def on_hover_arrow(self, e : ft.HoverEvent):
        if e.data == True:
            e.control.icon_color = self.page.theme.color_scheme.secondary
        else:
            e.control.icon_color = ft.Colors.WHITE
        e.control.update()

    def go_left(self, e):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.switcher.content = self.images_list[self.current_image_index]
            self.switcher.update()
        pass

    def go_right(self, e):
        if self.current_image_index < len(self.images_list) - 1:
            self.current_image_index += 1
            self.switcher.content = self.images_list[self.current_image_index]
            self.switcher.update()
        pass
    
    # PickFiles functions
    def get_images(self, product_name : str):
        images_paths = self.vm.get_images(product_name)
        print(f"Imagens encontradas para o produto '{product_name}': {images_paths}")

        image_list = []

        for path in images_paths:
            image_list.append(ft.Image(
                src=path,
                fit=ft.BoxFit.COVER,
                aspect_ratio=1,
                width=400 if self.page.width >= 400 else (self.page.width - 20),
            ))

        return image_list

    # Set to Clipboard
    async def set_to_clipboard(self, e):
        try:
            await ft.Clipboard().set(self.number_text.value)
            self.page.show_dialog(ft.SnackBar("Número copiado para a área de transferência!"))
        except Exception as e:
            self.page.show_dialog(ft.SnackBar("Não foi possível copiar o número."))
    pass
    
    def build(self):
        return ft.View(
            route= f"/Produto/{self.name}",
            scroll=ft.ScrollMode.AUTO,
            bgcolor="#fefae0",
            appbar=ft.AppBar(
                title=ft.Stack(
                    height=60,
                    controls=[
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text(
                                value=self.name,
                                font_family="Tangerine-Bold",
                                color=ft.Colors.BLACK,
                                size=50,
                            ),
                        ),
                    ],
                ),
            ),
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            border_radius=10,
                            alignment=ft.Alignment.CENTER,
                            padding=ft.Padding(bottom=20),
                            gradient=ft.LinearGradient(
                                begin=ft.Alignment(-1, -1),
                                end=ft.Alignment(1, 1),
                                colors=[
                                    self.page.theme.color_scheme.secondary_container,
                                    self.page.theme.color_scheme.primary_container,
                                ],
                            ),
                            shadow=ft.BoxShadow(
                                blur_radius=25,
                                color=ft.Colors.BLACK_38,
                                offset=ft.Offset(0, 8),
                            ),
                            content=ft.Column(
                                tight=True,  # <- faz a coluna ocupar só o necessário
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Stack(
                                        width=self.images_list[self.current_image_index].width,
                                        controls=[
                                            self.switcher,
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                vertical_alignment=ft.CrossAxisAlignment.END,
                                                controls=[
                                                    self.left_arrow,
                                                    self.right_arrow,
                                                ],
                                            ),
                                        ]
                                    ),

                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Encomende através do \nnosso WhatsApp!",
                                                size=30 if self.page.width >= 400 else 20,
                                                font_family="Montserrat",
                                                text_align=ft.TextAlign.CENTER,
                                                color=ft.Colors.WHITE,
                                            ),
                                        ],
                                    ),

                                    ft.Row(
                                        controls=[
                                            self.number_text,
                                        ]
                                    ),

                                    ft.Row(
                                        controls=[
                                            self.copy_button,
                                        ]
                                    )
                                ]
                            ),
                        )
                    ]
                ),
            ]
        )
pass