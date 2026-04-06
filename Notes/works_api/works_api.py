from fastapi import FastAPI,Request
from dtos import WorksDTO

works=[]
app = FastAPI()

# CRUD OPERATIONS : GET,POST,PUT,DELETE 

# CREATE WORKS
@app.post("/create_works")
def create_works(work_data:WorksDTO):
    work_data=work_data.model_dump()
    works.append(work_data)
    return {"status":"work successfully added","added work":work_data,"all works":works}

# GET WORKS
@app.get("/get_works")
def get_works():
    return works
@app.get("/get_works/{work_id}")
def get_one_work(work_id:int):
    for index,OneWork in enumerate(works):
        if OneWork.get("work_id")==work_id:
            return works[index]
    return {f"work with id {work_id}":"not found in database"}


# UPDATE WORK 
@app.put("/update_work")
def update_work(work_data:WorksDTO,work_id:int):
    work_data=work_data.model_dump()
    for index,OneWork in enumerate(works):
        if OneWork.get("work_id")==work_id:
            works[index]=work_data
            return {"status":"successfully updated","previous_data":OneWork,"updated_data":work_data}
    return {"status":f"work with id {work_id} not found"}    

# DELETE WORK 
@app.delete("/delete_one_work/{work_id}")
def delete_product(work_id:int):
    for index,OneWork in enumerate(works):
        if OneWork.get("work_id")==work_id:
            del works[index]
            return {"status":"successfully deleted","deleted_work":OneWork}
    return {"status":f"work with id {work_id} not found"}   
