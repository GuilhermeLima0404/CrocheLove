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
            scroll=ft.ScrollMode.ALWAYS,
            bgcolor="#fefae0",
            spacing=20,
            appbar=ft.AppBar(
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
                                width=150,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                ),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            value="Adiministrador",
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
                ft.Container(
                    alignment=ft.Alignment.CENTER,
                    border=ft.Border(
                        bottom=ft.BorderSide(
                            color=self.page.theme.color_scheme.primary_container,
                            width=2,
                        )
                    ),
                    padding=50,
                    content=ft.Image(
                        src="crochelovelogo.png",
                        fit=ft.BoxFit.COVER,
                    ),
                ),
                ft.Container(
                    alignment=ft.Alignment.CENTER,
                    border_radius=10,
                    padding=20,
                    #bgcolor=self.page.theme.color_scheme.secondary_container,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(-1, -1),  # canto superior esquerdo
                        end=ft.Alignment(1, 1),      # canto inferior direito
                        colors=[
                            self.page.theme.color_scheme.surface,
                            self.page.theme.color_scheme.secondary_container,
                            self.page.theme.color_scheme.surface,
                        ],
                        stops=[0.0, 0.5, 1.0],  # Define onde cada cor começa e termina
                    ),
                    content=ft.Text(
                        value="Bem-vindo à Crochê Love! Explore nossos produtos e encontre o presente perfeito para quem você ama 🩷",
                        text_align=ft.TextAlign.CENTER,
                        font_family="Montserrat",
                        size=30 if self.page.width >= 800 else 20,
                        color=ft.Colors.BLACK,
                    ),
                ),
                ft.GridView(
                    expand=True,
                    aspect_ratio=1,
                    max_extent=220,  # tamanho de cada card
                    spacing=30,
                    run_spacing=30,
                    controls=[
                        Product(self.page, name, path, adm_mode=False).build()
                        for name, path in self.page.data.dict_products_path.items()
                    ],
                )
            ],
        )
pass