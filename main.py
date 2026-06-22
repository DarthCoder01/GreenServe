from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from carbon_service import fetch_current_carbon
from scheduler import scheduler_decision
from queue_manager import *

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():

    carbon = fetch_current_carbon()

    decision = scheduler_decision(carbon)

    return {
        "carbon": carbon,
        "decision": decision
    }

@app.get("/queue")
def queue():

    return get_queue()

@app.post("/submit/{priority}")
def submit(priority):

    return add_job(priority)
