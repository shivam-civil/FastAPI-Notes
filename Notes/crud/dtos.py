from pydantic import BaseModel
from fastapi import FastAPI

class ProductDTO(BaseModel):
    id:int
    title:str
    category:str
    price:int
