from database.entity.employee import Employee
from database.database import session

from utils import toJson


class EmployeeC:
    def getDatas():
        return toJson(session.query(Employee).all(), Employee)
