from fastapi import APIRouter, HTTPException
from schema.patient import Patient, PatientCreate, patients 
from services.patient_service import PatientService

patient_router = APIRouter()


@patient_router.get("/", status_code=200)
def get_patient():
    data = PatientService.get_patients()
    return data

@patient_router.post("/", status_code=201)
def create_patient(payload: PatientCreate):
    data = PatientService.create_patient(payload)
    return {'message': 'Patient created successfully', 'data': data}
    
@patient_router.get('/{id}', status_code=200)
def get_patient_by_id(patient_id: int):
    data = PatientService.get_patient_by_id(patient_id)
    return {'message': 'Successfully fetched', 'data': data}       
                        
@patient_router.put("/{id}", status_code=200)
def update_patient(patient_id: int, payload: PatientCreate):
    data = PatientService.update_patient(payload)
    return {'message': 'Patient updated successfully', 'data': data}   
        
@patient_router.delete("/{id}", status_code=200)
def delete_patient(patient_id: int):
    PatientService.delete_patient(patient_id)
    return {'message': 'Patient deleted successfully', 'data': None}