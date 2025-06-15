from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
class Tea(BaseModel):
    id : int
    name : str
    origin : str

teas :List[Tea]   = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getTeas")
def getTeas():
    return teas

@app.post("/addTeas")
def addTeas(tea:Tea):
    teas.append(tea)
    return tea

@app.put("/addTeas/{tea_id}")
def addTeasWithId(tea_id:int,updated_tea: Tea):
    for index, tea in enumerate(tea):
        if tea.id == tea_id:
            tea[index] = Tea
            return updated_tea
    return {"error":"Tea not found"}

@app.put("/removeTeas/{tea_id}")
def addTeasWithId(tea_id:int,updated_tea: Tea):
    for index, tea in enumerate(tea):
        if(tea.id==tea_id):
            deleted = teas.pop(index)
            return deleted
    return {"error":"Tea not found"}


