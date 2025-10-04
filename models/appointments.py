from pydantic import BaseModel

class DoctorSlot(BaseModel):
    doctor_id:str
    slot_time:str
    status:str

class PatientBooking(BaseModel):
    patient_id:str
    slot_id:str

