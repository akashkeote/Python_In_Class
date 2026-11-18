import json

from fastapi import FastAPI,Path,HTTPException


app = FastAPI()


@app.get("/")
def home():
    return {"home": "this is home route"}


# path parameter in retieve update or delete me
def load_data():
    with open("employees.json","r") as f:
        data=json.load(f)
        return data
# @app.get("/employees/{employee_id}")
# def view(employee_id: str):
#     employees = load_data()["employees"]
#     if employee_id in employees:
#         return employees[employee_id]
#     return {"error": "employee not found"}


@app.get("/employees/{employee_id}")
def view_emp(employee_id:str=Path(...,description="Id of emp",example='1')):
    data=load_data()
    if employee_id in data:
        return data[employee_id]
    raise HTTPException(status_code=404,detail='AKasg No Found')
    
    
    
