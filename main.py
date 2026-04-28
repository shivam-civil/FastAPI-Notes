from fastapi import FastAPI,Request 
from dtos import ProductDTO 

products=[
    {
        "product_id":1,
        "name":"Apple",
        "cost":150,
        "sold":10
    },
    {
        "product_id":2,
        "name":"Mango",
        "cost":250,
        "sold":12
    }
]
app = FastAPI()

# GET ALL PRODUCTS 
@app.get("/get_products")
def get_products():
    return products 

# GET 1 PRODUCT WITH ID (QUERY PARAMS)
@app.get("/get_product_by_id")
def get_product_by_id(product_id:int):
    for oneProduct in products :
        if oneProduct["product_id"]==product_id : 
            return {"status":f"product with id {product_id} found","product":oneProduct}
    return {"status":f"product with id {product_id} not found",}    

# GET 1 PRODUCT WITH NAME  (PATH PARAMMS)
@app.get("/get_product_by_name/{name}")
def get_product_by_name(name:str):
    for oneProduct in products :
        if oneProduct["name"]==name :
            return {"status":f"product with name {name} found","product":oneProduct}
    return {"status":f"product with name {name} not found"}    

# GET PRODUCT BY ID AND NAME (REQUEST PARAMMS)
@app.get("/get_product_by_id_and_name")
def get_product_by_id_and_name(product_data: Request):
    product_data = dict(product_data.query_params)
    product_id = product_data.get("product_id")
    for oneProduct in products :
        if oneProduct["product_id"]==int(product_id) :
            return {"status":"product found","product":oneProduct}
    return {"status":"product not found"}    


# CREATE PRODUCT 
@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"status":"product added","added product details":product_data}

# DELETE PRODUCT BY ID (PATH PARAMMS )
@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index,oneProduct in enumerate(products) :
        if oneProduct["product_id"]==product_id :
            del products[index]
            return {"status":"product deleted"}
    return {"status":f"product with id {product_id}, not found and can't be deleted "}    



# UPDATE THE PRODUCT WITH ID 
@app.put('/update_product')
def update_product(product_id: int,product_data: ProductDTO):
    product_data = product_data.model_dump()
    for index,oneProduct in enumerate(products) :
        if oneProduct["product_id"]==product_id :
            prev_product = products[index]
            products[index]=product_data
            return {"status":f"product with id {product_id} updated","previous product":prev_product,"updated product":product_data}

