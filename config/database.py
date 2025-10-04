from pymongo import MongoClient

client = MongoClient("mongodb+srv://achujozefsl0709:KWQu2T2vSQZbPkDk@cluster0.pzwhnjm.mongodb.net/?retryWrites=true&w=majority")


db = client['appointment_booking_db']

doctor_slots = db['doctor_slots']

patient_bookings = db['patient_bookings']