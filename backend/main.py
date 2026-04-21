from fastapi import FastAPI

app = FastAPI()

@app.get("/phase_0")
def phase_0():
    return {"message": "This is phase 0"}

@app.get("/phase_1")
def phase_1():
    return {"message": "This is phase 1"}

@app.get("/phase_2")
def phase_2():
    return {"message": "This is phase 2"}

@app.get("/phase_3")
def phase_3():
    return {"message": "This is phase 3"}