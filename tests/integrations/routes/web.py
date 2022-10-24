from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/form", "WelcomeController@form")
]

ROUTES += Auth.routes()
