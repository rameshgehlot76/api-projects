# FastAPI Example 
# python 3.6+
# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI() 
@app.get('/')
def hello_world():
    return {'Hello':'World'} 

# 2nd
from fastapi import FastAPI 
app = FastAPI() 
@app.get("/items/") 
def read_word():
    return [{"name": "Ramesh"}, {"name": "Suresh"}]

# To run the server: uvicorn filename:app  --reload 
