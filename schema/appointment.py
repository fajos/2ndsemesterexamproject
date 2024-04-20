from pydantic import BaseModel
from datetime import datetime

class Appointment(BaseModel):
    id: int
    patient_name: str
    doctor_name: str
    date: datetime
    
class AppointmentCreate(BaseModel):
    patient_name: str
    doctor_name: str
    date: datetime
    
appointments: dict[int, Appointment] = {}