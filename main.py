from fastapi import FastAPI

from routers.patients import patient_router
from routers.doctors import doctor_router
from routers.appointments import appointment_router

app = FastAPI()

app.include_router(router=patient_router, prefix='/patients', tags=['Patients'])
app.include_router(router=doctor_router, prefix='/doctors', tags=['Doctors'])
app.include_router(router=appointment_router, prefix='/appointments', tags=['Appointments'])

@app.get('/')
async def greetings():
    return {'message': 'Welcome to Doctors-Patients Appointment Page'}