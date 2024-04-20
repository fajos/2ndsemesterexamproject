from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str
    
class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str
    
patients: dict[int, Patient] = {}