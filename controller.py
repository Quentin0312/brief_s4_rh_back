from database.entity.employee import Employee
from database.database import session

from utils import toJson


class EmployeeC:
    def getDatas():
        return toJson(session.query(Employee).all(), Employee)

    def addDatas(body):
        first_name = body["first_name"]
        last_name = body["last_name"]
        gender = body["gender"]
        phone = body["phone"]
        email_pro = body["email_pro"]
        email_perso = body["email_perso"]

        new_employee = Employee(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone=phone,
            email_pro=email_pro,
            email_perso=email_perso,
        )
        session.add(new_employee)
        session.commit()
        return "ok"

    def removeDatas(body):
        id = body["id"]

        session.query(Employee).filter(Employee.id == id).delete()
        session.commit()
        return "ok"
