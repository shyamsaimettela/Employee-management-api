from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Employee(BaseModel):
    id: int
    name: str
    department: str

employees = [
    {
        "id": 1,
        "name": "John",
        "department": "IT"
    },
    {
        "id": 2,
        "name": "Alice",
        "department": "HR"
    },
    {
        "id": 3,
        "name": "Nandu",
        "department": "Testing"
    }
]

@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management API"
    }

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return {"error": "Employee not found"}

@app.post("/employees")
def create_employee(employee: Employee):
    employees.append(employee.model_dump())
    return {
        "message": "Employee created successfully", 
            "employee": employee
        }
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):

    for index, employee in enumerate(employees):

        if employee["id"] == employee_id:

            employees[index] = updated_employee.model_dump()

            return {
                "message": "Employee updated successfully",
                "employee": updated_employee
            }

    return {
        "message": "Employee not found"
    }
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for index, employee in enumerate(employees):

        if employee["id"] == employee_id:

            deleted_employee = employees.pop(index)

            return {
                "message": "Employee deleted successfully",
                "employee": deleted_employee
            }

    return {
        "message": "Employee not found"
    }