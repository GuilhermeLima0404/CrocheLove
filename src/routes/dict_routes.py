# Importando as rotas #
from routes.routes import HOME, ADMIN, ADD_PRODUCT

# Importando os viewmodels #
from viewmodels.home_viewmodel import Home_viewmodel
from viewmodels.adm_viewmodel import Adm_viewmodel
from viewmodels.add_product_viewmodel import Add_product_viewmodel

# Importando os views #
from views.home_view import Home_view
from views.adm_view import Adm_view
from views.add_product_view import Add_product_view

dict_routes = {
    HOME : (Home_view, Home_viewmodel),
    ADMIN : (Adm_view, Adm_viewmodel),
    ADD_PRODUCT : (Add_product_view, Add_product_viewmodel),
}