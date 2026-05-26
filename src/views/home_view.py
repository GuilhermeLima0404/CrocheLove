import flet as ft
from routes.routes import HOME, ADMIN
from models.product import Product
from viewmodels.home_viewmodel import Home_viewmodel

class Home_view:
    def __init__(self, page : ft.Page, vm : Home_viewmodel):
        self.page = page
        self.vm = vm

        # Widgets
        self.password_field = ft.TextField(
            label="Digite a senha",
            password=True,
            can_reveal_password=True,
        )
        
        self.cupertino_alert_dialog = ft.CupertinoAlertDialog(
            title=ft.Text("Entrar na area do administrador"),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.password_field,
                    ft.ElevatedButton(
                        bgcolor=ft.Colors.WHITE,
                        color=ft.Colors.BLACK,
                        content=ft.Text("Entrar"),
                        on_click=self.handle_validate_password,
                    )
                ],
            ),
            on_dismiss=self.handle_dialog_dismissal,
        )
    pass
    
    # Alert dialog para validar a senha do administrador
    async def handle_validate_password(self, e):
        password = self.password_field.value
        self.handle_action_click(e)  # Fechar o diálogo

        if self.vm.validate_password(password):
            await self.go_to_adm_view()
        else:
            self.page.show_dialog(ft.SnackBar(content=ft.Text("Senha incorreta!")))

    def handle_dialog_dismissal(self,_: ft.Event[ft.DialogControl]):
        self.page.controls.append(ft.Text("Dialog dismissed"))

    def handle_action_click(self, e: ft.Event[ft.CupertinoDialogAction]):
        self.page.pop_dialog()

    # Navegar para a view de administrador
    async def go_to_adm_view(self):
        await self.page.push_route(ADMIN)
    
    def build(self):
        return ft.View(
            route=HOME,
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
                            alignment=ft.Alignment.CENTER_RIGHT,
                            content=ft.ElevatedButton(
                                bgcolor=ft.Colors.WHITE,
                                color="#8c53b3",
                                width=150,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                ),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            value="Adiministrador",
                                            color=ft.Colors.BLACK,
                                            font_family="Montserrat",
                                        ),
                                    ]
                                ),
                                on_click=lambda _: self.page.show_dialog(self.cupertino_alert_dialog),
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
                        Product(self.page, name, path, adm_mode=False).build()
                        for name, path in self.page.data.dict_products_path.items()
                    ],
                )
            ],
        )
pass