from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"voce esta na home": "Hello World!"}

