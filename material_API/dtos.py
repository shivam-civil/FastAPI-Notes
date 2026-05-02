from pydantic import BaseModel

class MaterialDTO(BaseModel):
    mat_id: int 
    name: str 
    quantity: float 
    unit: str
    imported_date: str 
    