from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.appointments  import appointment_router
app = FastAPI()


origins = [
    "http://localhost",  
    "http://localhost:3000",  
  
]



app.include_router(appointment_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)