import pandas as pd
from database import session
from entity.employee import Employee

# TODO: replace relative path with absolute path
dataCSV = pd.read_csv("datacsv/data.csv")

# TODO: replace NaN with undefined to have null corresponding value in database
for i in range(0, len(dataCSV)):
    newEmployee = Employee(
        first_name=dataCSV.iat[i, 1],
        last_name=dataCSV.iat[i, 2],
        gender=dataCSV.iat[i, 3],
        phone=dataCSV.iat[i, 4],
        email_pro=dataCSV.iat[i, 5],
        email_perso=dataCSV.iat[i, 6],
    )
    session.add(newEmployee)
    session.commit()
