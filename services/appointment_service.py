from fastapi import HTTPException
from datetime import date

from schema.appointment import Appointment, AppointmentCreate, appointments
from services.doctor_service import DoctorService
from services.patient_service import PatientService
from schema.patient import patients
from schema.doctor import doctors

appointment_counter: int = 0


class AppointmentService:
    doctor_service = DoctorService()
    patient_service = PatientService()
    
    @staticmethod
    def get_appointment_by_id(appointment_id):
        appointment = appointments.get(appointment_id)
        if appointment is None:
            raise HTTPException(detail = 'appointment not found', status_code=404)
        return appointment
    
    @staticmethod
    def create_appointment(id: int):
        global appointment_counter
        patient = patients.get(id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
    
        available_doctors = [doctor for doctor in doctors.values() if doctor.is_available]
        if not available_doctors:
            raise HTTPException(status_code=400, detail="No available doctors")
    
        selected_doctor = available_doctors[0]  # Select the first available doctor
        appointment_counter += 1
        appointment = Appointment(id=appointment_counter, patient_name=patient.name, doctor_name=selected_doctor.name, date="2024-04-20")
        appointments[appointment_counter] = appointment
        selected_doctor.is_available = False  # Set the doctor as unavailable
        return appointment
    
    @staticmethod
    def complete_appointment(id: int):
        appointment = appointments.get(id)
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
    
        doctor = doctors.get(appointment.doctor_name)
        if doctor:
            doctor.is_available = True  # Set the doctor as available again
        
    @staticmethod
    def cancel_appointment(id: int):
        appointment = appointments.pop(id, None)
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
    
        doctor = doctors.get(appointment.doctor_name)
        if doctor:
            doctor.is_available = True  # Set the doctor as available again