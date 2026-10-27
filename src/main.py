from fastapi import FastAPI
from src.controllers.transaction import router as transaction_router

app = FastAPI(
    title="Transactions API",
    description="Microservice to maintain withdrawal and deposit operations from current accounts.",
    version="1.0.0"
)

app.include_router(transaction_router)

@app.get("/")
def read_root():
    return {"message": "API Bancaria Assincrona Ativa. Acesse /docs para o Swagger."}
