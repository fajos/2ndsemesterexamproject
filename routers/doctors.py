from fastapi import APIRouter
from schema.doctor import DoctorCreate, doctors
from services.doctor_service import DoctorService   

doctor_router = APIRouter()

@doctor_router.get('/', status_code=200)
def get_doctor():
    return doctors

@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorCreate):
    data = DoctorService.create_doctor(payload)
    return {'message': 'Doctor created successfully', 'data': data}
    
@doctor_router.get('/{id}', status_code=200)
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'Doctor retrieved successfully', 'data': data}
    
@doctor_router.put('/{id}', status_code=200)
def update_doctor(doctor_id: int, payload: DoctorCreate):
    data = DoctorService.update_doctor(doctor_id, payload)
    return {'message': 'Doctor updated successfully', 'data': data}
    
@doctor_router.delete('/{id}', status_code=200)
def delete_doctor(doctor_id: int):
    DoctorService.delete_doctor(doctor_id)
    return {'message': 'Doctor deleted successfully', 'data': None}
    
@doctor_router.put("/doctors/{doctor_id}/set-availability/")
def set_doctor_availability(id: int, is_available: bool):
    DoctorService.set_doctor_availability(id, is_available)
    return {'message': f'Doctor {id} availability is set to {is_available}'}