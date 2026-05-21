import flet as ft

# Importando as rotas #
from routes.dict_routes import dict_routes
from routes.routes import HOME, LOGIN
from models.app import App_data
from services.database_manager import get_app_data

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

    app : App_data = get_app_data()

    page.data = app

    print("Initial route:", page.route)

    def route_change():
        print("Route change:", page.route)
        page.views.clear()

        # Adicionando Home page
        page.views.append(dict_routes.get(HOME)(page).build())

        # Adicionando a nova route
        if page.route != HOME:
            page.views.append(dict_routes.get(page.route)(page).build())
        
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
    ft.run(main, assets_dir="assets")