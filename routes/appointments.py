from fastapi import APIRouter
from models.appointments import DoctorSlot , PatientBooking
from config.database import db



appointment_router = APIRouter()

@appointment_router.post("/doctors/{doctor_id}/slots")
async def add_doctor_slot(doctor_id:str,slot:DoctorSlot):
    slot_data = slot.dict()
    slot_data["doctor_id"]=doctor_id
    db.doctor_slots.insert_one(slot_data)
    return slot

@appointment_router.get("/doctor/{doctor_id}/slots")
async def get_doctor_slots(doctor_id:str):
    slots= list(db.doctor_slots.find({"doctor_id":doctor_id}))
    for slot in slots:
        slot["_id"] = str(slot["_id"])
    return slots

@appointment_router.post("/patients/book") 
async def book_slot(booking:PatientBooking):
    booking_date = booking.dict()
    db.patient_booking.insert_one(booking_date)
    db.doctor_slots.update_one(
        {"_id":booking.slot_id},
        {"$set":{"status":"booked"}}
    )
    return booking

@appointment_router.put("/doctor/confirm")
async def confirm_booking (booking : PatientBooking):
    db.doctor_slot.update_one(
        {"_id":booking.slot_id},
        {"$set":{"status":"confirmed"}}
    )
    return booking

@appointment_router.delete("/doctor/{slot_id}/delete")
async def delete_slot(slot_id:str):
     db.doctor_slot.find_one_and_delete({"_id":slot_id})
     return{"message":"Slot Deleted successfully"}