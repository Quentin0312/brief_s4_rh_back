import hug

from hug.middleware import CORSMiddleware

from controllers.controller import HelloWorld

api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=["*"]))

api_base_url = "/api"

hug.get(api_base_url + "/hello_world", api=api)(HelloWorld.sayHello)
# hug.get(api_base_url + "/", api=api)()
