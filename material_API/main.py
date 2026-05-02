# MATERIALS CRUD API 

from fastapi import FastAPI,Path,Query,HTTPException
from dtos import MaterialDTO
import json 
def load_data():
    with open("materials.json","r") as f:
        return json.load(f)
    
def update_data(new_data):
    with open("materials.json","w") as f :
        json.dump(new_data,f,indent=4)



app = FastAPI()

@app.get("/get_materials") # GET MATERIALS ENDPOINT WITH QUERY PARAMMS
def get_materials(mat_id:int = Query(None,description="material_id of material",example=1),reverse:str = Query("false",description="true")):
    data = load_data()
    if not mat_id and mat_id!=0 :
        if reverse.strip().lower()=="true":
            return list(reversed(data))
        return data
    for material in data :
        if material["mat_id"]==mat_id:
            return {'status':f"material with id {mat_id} found","material details":material}
    raise HTTPException(status_code=404,detail=f"material with id {mat_id} not found")


@app.get("/get_items/{mat_id}/")  # GET SPECIFIC MATERIAL DETAILS BY ID (PATH PARAMMS)
def get_items(mat_id:int = Path(...,description="Material ID ",example="1")):
    data=load_data()
    if mat_id :
        for mat in data:
            if mat["mat_id"]==mat_id :
                return {"status":f"material with id {mat_id} found","material details":mat}
        raise HTTPException(status_code=404,detail=f"Material of id {mat_id} not found")    
    

@app.post("/create_material")       # CREATE MATERIAL ENDPOINT 
def create_material(mat_data: MaterialDTO):
    mat_data = mat_data.model_dump()
    data = load_data()
    try:
        data.append(mat_data)
        update_data(data)
        return {"status":"material added success","added material details":mat_data,"add materials details":data}
    except :
        return HTTPException(status_code=404,detail="error occured in try/except block")    
    
@app.delete("/delete_material")     # DELETE MATERIAL ENDPOINT (QUERY PARAMMS)
def delete_material(mat_id:int = Query(None,description="Material ID",example=1,title="MAtIDTitle")):
    if not mat_id :
        raise HTTPException(status_code=404,detail="the endpoint wont get material id to delete")
    data = load_data()
    for index,mat in enumerate(data) :
        if mat["mat_id"]==mat_id :
            del data[index]
            update_data(data)
            return {"status":"material deleted success","deleted material":mat,"remaining materials":data}
    raise HTTPException(status_code=404,detail=f"material with {mat_id} id not found and can't be deleted")
         

@app.put("/update_material")  # UPDATE MATERIAL ENDPOINT (QUERY PARAMMS)
def update_material(mat_data: MaterialDTO,mat_id: int = Query(None,description="Material ID",example="1")):
    if not mat_id :
        raise HTTPException(status_code=404,detail="material id must be sent via query paramms of update endpoint")
    mat_data = mat_data.model_dump()
    data = load_data()
    for index,mat in enumerate(data) :
        if mat["mat_id"]==mat_id :
            data[index]=mat_data
            update_data(data)
            return {"status":200,"detail":"material updated","material updated at index":index,"all materials ":data}
    raise HTTPException(status_code=404,detail="material with id {mat_id} not found and can't be updated")    

    

