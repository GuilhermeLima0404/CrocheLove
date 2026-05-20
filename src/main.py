import flet as ft

# Importando as rotas #
from routes.dict_routes import dict_routes
from routes.routes import HOME, LOGIN

def main(page: ft.Page):
    page.title = "Croche Love"

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
    ft.run(main)