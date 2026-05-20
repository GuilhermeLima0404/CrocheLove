from routes.routes import HOME, LOGIN
from views.home_view import Home_view
from views.login_view import Login_view

dict_routes = {
    HOME : Home_view,
    LOGIN : Login_view,
}
