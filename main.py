from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Data Management API",
    description="API REST para la ingesta y consulta de registros analíticos.",
    version="1.0.0"
)

class DataRecord(BaseModel):
    id: int
    sensor_id: str
    value: float
    status: str

db_records: List[DataRecord] = []

@app.get("/", tags=["Health Check"])
def root():
    return {"status": "online", "message": "Data Management API operando correctamente."}

@app.post("/records/", response_model=DataRecord, tags=["Data Ingestion"])
def create_record(record: DataRecord):
    db_records.append(record)
    return record

@app.get("/records/", response_model=List[DataRecord], tags=["Analytics Query"])
def get_records():
    return db_records
