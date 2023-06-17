import hug

from hug.middleware import CORSMiddleware
from controller import EmployeeC

api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=["*"]))

api_base_url = "/api/employee"


class Test:
    def returnNone():
        return None


hug.get(api_base_url, api=api)(EmployeeC.getDatas)

# TODO: bandage the POST request issue and change it to PATCH or else ! => DONT work
hug.post(api_base_url, api=api)(EmployeeC.addDatas)
# hug.patch(api_base_url, api=api)(EmployeeC.addDatas)

hug.delete(api_base_url, api=api)(EmployeeC.removeDatas)
hug.put(api_base_url, api=api)(EmployeeC.modifyDatas)
