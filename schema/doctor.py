from pydantic import BaseModel


class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str  
    is_available: bool = True
    
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: bool = True
    

doctors: dict[int, Doctor] = {}