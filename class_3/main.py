from fastapi import FastAPI
from routes.hello import router as hello_router

app = FastAPI()
app.include_router(hello_router)

@app.get("/")
def root():
    return {"message": "Welcome to the API"}