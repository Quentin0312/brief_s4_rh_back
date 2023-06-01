import hug

from hug.middleware import CORSMiddleware
from controller import EmployeeC

api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=["*"]))

api_base_url = "/api"

hug.get(api_base_url + "/employee", api=api)(EmployeeC.getDatas)
hug.post(api_base_url + "/employee", api=api)(EmployeeC.addDatas)
hug.delete(api_base_url + "/employee", api=api)(EmployeeC.removeDatas)
