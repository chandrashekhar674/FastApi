from fastapi import FastAPI

app = FastAPI()

#/users?name=mohit
#products?price=1000

@app.get("/users")# optional filter
def get_users(name: str = None): 
    return{"Name":name}

@app.get("/products")# for defualt value
def get_users(limit: int = 10):
    return {"Limit":limit}

@app.get("/items")# for multiple filter
def get_users(name: str = None, price: int=0):
    return {
        "name":name,
        "price":price
    }