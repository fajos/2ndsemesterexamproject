from fastapi import HTTPException

from schema.patient import PatientCreate, Patient, patients

class PatientService:
    
    @staticmethod
    def get_patients():
        return patients
    
    @staticmethod
    def get_patient_by_id(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail = 'patient not found', status_code=404)
        return patient
    
    @staticmethod
    def create_patient(patient_data: PatientCreate):
        id=len(patients)
        patient = Patient(id=id,**patient_data.model_dump())
        patients[id] = patient   
        return patient
    
    @staticmethod
    def update_patient(payload: PatientCreate): 
        id = len(patients)
        patient = Patient(id=id,**payload.model_dump())
        patients[id] = patient
        return patient
    
    @staticmethod
    def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail = 'patient not found', status_code=404)
        del patients[patient_id]

    