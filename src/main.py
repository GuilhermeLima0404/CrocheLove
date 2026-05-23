# Arquivo main.py #
import flet as ft

# Importando as rotas #
from routes.dict_routes import dict_routes
from routes.routes import ADMIN, HOME, REFRESH

# Importando os viewmodels #
from viewmodels.home_viewmodel import Home_viewmodel
from viewmodels.adm_viewmodel import Adm_viewmodel  

# Importando os models #
from models.app import App_data

# Importando os serviços #
from services.database_manager import get_app_data

# Construtor de views
def get_view(route : str, pg : ft.Page) -> ft.View:
    view_class, vm_class = dict_routes.get(route)

    vm = vm_class(pg.data)
    view = view_class(pg, vm)

    return view

def main(page: ft.Page):
    page.title = "Croche Love"

    # Configurando o diretório de assets para a pasta "assets"
    page.assets_dir = "assets"

    # Registrando o nome da fonte
    page.fonts = {
        "Tangerine": "fonts/Tangerine-Regular.ttf",
        "Montserrat": "fonts/Montserrat-Regular.ttf",
    }

    # Configurando o thema da aplicação
    page.theme = ft.Theme(
        font_family="Montserrat"
    )

    # Lendo as infos do app
    app : App_data = get_app_data()
    page.data = app

    print("Initial route:", page.route)

    def route_change():
        print("Route change:", page.route)
        page.views.clear()

        # Adicionando Home page
        view = get_view(HOME, page)
        page.views.append(view.build())

        # Adicionando a nova route
        if page.route != HOME:
            if page.route == REFRESH:
                page.data = get_app_data()
                view = get_view(ADMIN, page)
                page.views.append(view.build())
            else:
                page.data = get_app_data()
                view = get_view(page.route, page)
                page.views.append(view.build())
        
        page.update()

    async def view_pop(e):
        if e.view is not None:
            print("View pop:", e.view)
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

if __name__ == "__main__":
    ft.run(main, assets_dir="assets", upload_dir="assets/uploads")