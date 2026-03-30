from pydantic import BaseModel 
from fastapi import FastAPI 

class WorksDTO(BaseModel):
    work_id:int
    title:str
    estimated_price:float
    actual_price:float

    
