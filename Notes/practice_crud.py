# CRUD OPERATIONS USING REQUEST AND WORKDTO DTO IN FASTAPI

from fastapi import FastAPI,Request
from dtos import WorkDTO


app = FastAPI()
works = []

# GET METHOD TO ONE SPECIFIC ID WORK  (QUERY PARAMMS)
@app.get("/get_work")
def get_work(work_para: Request):
    work_para = dict(work_para.query_params)
    work_id = work_para.get("work_id")
    name = work_para.get("name")
    for index,OneWork in enumerate(works):
        if OneWork.get("work_id") == int(work_id) and OneWork.get("name")==name :
            return works[index]
        
    return {"status":f"work with id {work_id} not found"}    


# POST METHOD TO ADD WORK BY SENDING DATA IN RAW JSON FORMAT FROM POSTMAN BODY TO API
@app.post("/add_work")
def add_work(work_data: WorkDTO) :
    work_data = work_data.model_dump()
    works.append(work_data)
    return {"status":"work added","added work":work_data,"all works":works}


# UPDATE WORK BY ID AND [ DATA AS PATH PARAMMS ]
@app.put("/update_work/{work_id}")
def update_work(update_data: WorkDTO,work_id:int ) :
    update_data = update_data.model_dump()
    for index,OneWork in enumerate(works):
        if OneWork.get("work_id") == work_id :
            works[index] = OneWork
            return {"status":f"work of id {work_id} updated.","updated data ":update_data}
        
    return {"status":f"work of id {work_id} not updated"}    

# DELETE WORK BY ID PASSING THROUGH PATH PARAMMS 
@app.delete("/delete_work/{work_id}")
def delete_work(work_id:int):
    for index,OneWork in enumerate(works):
        if OneWork.get("work_id") == work_id :
            del works[index]
            return {"status":"work of id {work_id} deleted successfully."}
        
    return {"status":f"not deleted data of id {work_id}"}  


"""
INSIDE DTOS.PY

from pydantic import BaseModel

class WorkDTO(BaseModel):
    work_id : int 
    name : str
    cost : float
    


"""

