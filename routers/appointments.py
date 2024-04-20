from fastapi import APIRouter, HTTPException
from datetime import date

from schema.appointment import Appointment, AppointmentCreate, appointments
from services.appointment_service import AppointmentService
from services.doctor_service import DoctorService

appointment_counter: int = 0

appointment_router = APIRouter()

@appointment_router.get('/', status_code=200)
def get_appointment():
    return appointments

@appointment_router.post('/', status_code=201)
def create_appointment(patient_id: int):
    data = AppointmentService.create_appointment(patient_id)
    return {'message': 'Appointment created successfully', 'data': data}

@appointment_router.put("/{appointment_id}/complete/")
def complete_appointment(appointment_id: int):
    AppointmentService.complete_appointment(appointment_id)
    return {"message": f"Appointment {appointment_id} completed."}

@appointment_router.delete("/appointments/{appointment_id}/cancel/", status_code=200)
def cancel_appointment(appointment_id: int):
    AppointmentService.cancel_appointment(appointment_id)
    return {'message': f'Appointment {appointment_id} canceled'}