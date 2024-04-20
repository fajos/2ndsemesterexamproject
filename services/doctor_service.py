from fastapi import HTTPException

from schema.doctor import DoctorCreate, Doctor, doctors

class DoctorService:
    
    
    @staticmethod
    def get_doctors():
        return doctors
    
    @staticmethod
    def get_doctor_by_id(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail = 'doctor not found', status_code=404)
        return doctor
    
    @staticmethod
    def create_doctor(doctor_data: DoctorCreate):
        id=len(doctors)
        doctor = Doctor(id=id,**doctor_data.model_dump())
        doctors[id] = doctor   
        return doctor
    
    @staticmethod
    def update_doctor(payload: DoctorCreate): 
        id = len(doctors)
        doctor = Doctor(id=id,**payload.model_dump())
        doctors[id] = doctor
        return doctor
    
    @staticmethod
    def set_doctor_availability(id: int, is_available: bool):
        doctor = doctors.get(id)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
 
        doctor.is_available = is_available
    
    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
             raise HTTPException(detail = 'patient not found', status_code=404)
        del doctors[doctor_id]