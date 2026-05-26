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
            bgcolor=ft.Colors.WHITE,
            color="#8c53b3",
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
            value="+55 51 8150-2727",
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
            e.control.icon_color = "#8c53b3"
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
                width=400,
                height=400,
            ))

        return image_list

    # Set to Clipboard
    async def set_to_clipboard(self, e):
        await ft.Clipboard().set(self.number_text.value)
        self.page.show_dialog(ft.SnackBar("Número copiado para a área de transferência!"))

    def build(self):
        return ft.View(
            route= f"/Produto/{self.name}",
            scroll=ft.ScrollMode.AUTO,
            bgcolor=ft.Colors.WHITE,
            appbar=ft.AppBar(
                bgcolor="#4cc9f0",
                elevation=0,
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
                                value=self.name,
                                font_family="Tangerine",
                                color=ft.Colors.BLACK,
                                size=50,
                            ),
                        ),
                    ],
                ),
            ),
            controls=[
                ft.Row(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=400,
                            height=600,
                            border_radius=10,
                            bgcolor="#8c53b3",
                            alignment=ft.Alignment.CENTER,
                            shadow=ft.BoxShadow(
                                blur_radius=25,
                                color=ft.Colors.BLACK_38,
                                offset=ft.Offset(0, 8),
                            ),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                        expand=True,
                                        controls=[
                                            ft.Stack(
                                                width=400,
                                                height=400,
                                                controls=[
                                                    self.switcher,
                                                    ft.Container(
                                                        bottom=0,
                                                        width=400,
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            controls=[
                                                                self.left_arrow,
                                                                self.right_arrow,
                                                            ],
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ],
                                    ),
        
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                        controls=[
                                            ft.Text(
                                                value="Encomende através do \nnosso WhatsApp!",
                                                size=30,
                                                font_family="Montserrat",
                                                text_align=ft.TextAlign.CENTER,
                                                color=ft.Colors.WHITE,
                                            ),
                                        ],
                                    ),
        
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                        controls=[
                                            self.number_text,
                                        ]
                                    ),
        
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                        margin=ft.Margin(0, 0, 0, 20),
                                        controls=[
                                            self.copy_button,
                                        ]
                                    )
                                ]
                            ),
                        ),
                    ]
                ),
            ]
        )
        
        
pass