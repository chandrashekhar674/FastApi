from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello without vern"}

@app.get("/about")
def about():
    return{"message":"This is About Page"}

@app.get("/users")
def users():
    return {
        "users":["mohit","Rohit","Amit"]
    }

@app.get("/home")
def users():
    return {
        "message":"This is Home page"
    }