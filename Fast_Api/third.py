# Path parameter
from fastapi import FastAPI,Path
import json

app = FastAPI()


def load_data():
    with open("patients.json","r") as f:
        return json.load(f)


@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    # Load all patients.
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {"error": "patient not found"}

