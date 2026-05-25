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
            icon=ft.Icons.ARROW_RIGHT, 
            on_click=self.go_right, 
            on_hover=self.on_hover_arrow, 
            bgcolor=ft.Colors.TRANSPARENT, 
            icon_color=ft.Colors.BLACK,
            height=100,
            width=100,
            icon_size=50,
        )

        self.left_arrow = ft.IconButton(
            icon=ft.Icons.ARROW_LEFT, 
            on_click=self.go_left, 
            on_hover=self.on_hover_arrow, 
            bgcolor=ft.Colors.TRANSPARENT, 
            icon_color=ft.Colors.BLACK,
            height=100,
            width=100,
            icon_size=50,
        )

        self.switcher = ft.AnimatedSwitcher(
            content = self.images_list[0],
            duration=500,
            reverse_duration=500,
        )
        pass
    
    def on_hover_arrow(self, e):
        if e.data == "true":
            e.control.opacity = 0.5
        else:
            e.control.opacity = 1.0
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


    def build(self):
        return ft.View(
            route= f"/Produto/{self.name}",
            scroll=ft.ScrollMode.AUTO,
            bgcolor=ft.Colors.WHITE,
            align=ft.Alignment.CENTER,
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
                            value=self.name,
                            size=40,
                        ),
                    ],
                )
            ),
            controls=[
                ft.Container(
                    width=400,
                    height=600,
                    border_radius=10,
                    bgcolor="#4cc9f0",
                    alignment=ft.Alignment.CENTER,
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
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    self.left_arrow,
                                                    self.right_arrow,
                                                ],
                                            ),
                                        ]
                                    ),
                                ],
                            ),

                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.START,
                                expand=True,
                                controls=[
                                    ft.Text(
                                        value=f"{self.name}",
                                        size=20,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                            ),
                        ]
                    ),
                ),
            ]
        )
        
        
pass