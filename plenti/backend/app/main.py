from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Plenti API'ye Hoş Geldiniz!"} 