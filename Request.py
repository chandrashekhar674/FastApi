from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# @app.post("/create_user")# Normal Approach
# def create_user(name:str, age:int):
#     return{
#         "name":name,
#         "age":age
#     }
# class User(BaseModel):# use for pydantic to define feilds
#     name:str
#     age:int
#     email:str

# @app.post("/create_user")# Real  Approach
# def create_user(user:User):
#     return{
#         "message":"User Created ",
#         "Data":user
 
#     }

#Nasted Model
class Address(BaseModel):
    city:str
    pincode:int



class User(BaseModel):# use for pydantic to define feilds
    name:str
    age:int
    email:str
    address:Address
    

@app.post("/create_user")# Real  Approach
def create_user(user:User):
    return{
        "message":"User Created ",
        "Data":user
 
    }

