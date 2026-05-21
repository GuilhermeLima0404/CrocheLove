# Importando as rotas #
from routes.routes import HOME, ADMIN

# Importando os viewmodels #
from viewmodels.adm_viewmodel import Adm_viewmodel
from viewmodels.home_viewmodel import Home_viewmodel

# Importando os views #
from views.home_view import Home_view
from views.adm_view import Adm_view

dict_routes = {
    HOME : (Home_view, Home_viewmodel),
    ADMIN : (Adm_view, Adm_viewmodel),
}