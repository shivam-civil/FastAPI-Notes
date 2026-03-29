from dtos import ProductDTO
from fastapi import FastAPI

products=[]
app = FastAPI()

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data=product_data.model_dump()
    products.append(product_data)
    return {"status":"Product Added Successfully","added_product":product_data,"total_products":products}

@app.get("/get_products")
def get_products():
    return products

@app.put("/update_products")
def update_products(product_data:ProductDTO):
    product_data=product_data.model_dump()
    for index,OneProduct in enumerate(products):
        if OneProduct.get("id")==product_data.get("id"):
            products[index]=product_data
            return products
        
@app.delete("/delete_products/{id}")
def delete_products(product_data:ProductDTO,id:int):
    product_data=product_data.model_dump()
    for index,OneProduct in enumerate(products):
        if OneProduct.get("id")==id:
            del products[index]
            return {"status":400,"product_deleted":product_data,"remaining_products":products}  
    return {"status":422}    