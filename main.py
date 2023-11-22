from fastapi import FastAPI

app = FastAPI()


@app.get("/Sum/{a}/{b}")
def calculated_plus(a: float, b: float):
    return {"Sum ==": a+b}


@app.get("/Difference/{a}/{b}")
def calculated_minus(a: float, b: float):
    return {"Difference ==": a-b}


@app.get("/Division/{a}/{b}")
def calculated_division(a: float, b: float):
    return {"Division ==": a/b}


@app.get("/Multiplication/{a}/{b}")
def calculated_multiplication(a: float, b: float):
    return {"Multiplication ==": a*b}