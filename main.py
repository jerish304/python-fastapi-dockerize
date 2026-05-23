from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Product Model
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int


# Sample Products
products = [
    Product(id=1, name="Phone", description="Budget Phone", price=10000.00, quantity=2),
    Product(id=2, name="Laptop", description="Mac", price=40000.00, quantity=5),
    Product(id=3, name="Fridge", description="Cool at 16 degree", price=16000.00, quantity=8),
    Product(id=4, name="AC", description="heater and cooler", price=20000.00, quantity=9)
]


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI project"}


@app.get("/products")
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product

    return {"message": "No product found"}


@app.post("/product")
def add_product(product: Product):
    products.append(product)

    return {
        "message": "Product added successfully",
        "product": product
    }


@app.delete("/product/{id}")
def delete_product(id: int):
    global products

    products = [product for product in products if product.id != id]

    return {"message": f"Product with id {id} deleted"}