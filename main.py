import os

# Estrutura isolada em texto puro para o compilador não tentar importar nada
projeto_bancario = {
    "src/config.py": """from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")
    database_url: str = "sqlite+aiosqlite:///./bank.db"
    environment: str = "production"
    jwt_secret_key: str = "supersecretkey"
    jwt_algorithm: str = "HS256"

settings = Settings()
""",
    "src/models/bank.py": """from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class AccountModel(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    holder_name = Column(String)
    balance = Column(Float, default=0.0)
    transactions = relationship("TransactionModel", back_populates="account")

class TransactionModel(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    type = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    account = relationship("AccountModel", back_populates="transactions")
""",
    "src/controllers/transaction.py": """from fastapi import APIRouter, HTTPException, status

router = APIRouter(tags=["transaction"])

@router.post("/accounts/{account_id}/transactions", status_code=status.HTTP_201_CREATED)
async def create_transaction(account_id: int, type: str, amount: float):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="O valor da operacao deve ser maior que zero.")
    if type.upper() not in ["DEPOSIT", "WITHDRAWAL"]:
        raise HTTPException(status_code=400, detail="Tipo de operacao invalido. Use DEPOSIT ou WITHDRAWAL.")
    return {"message": "Transacao registrada com sucesso no barramento assincrono."}

@router.get("/accounts/{account_id}/transactions")
async def read_account_transactions(account_id: int):
    return {"account_id": account_id, "transactions": []}
""",
    "src/main.py": """from fastapi import FastAPI
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
""",
    ".gitignore": ".env\n*.db\n__pycache__/\n.venv/\n",
    ".env.example": "DATABASE_URL=sqlite+aiosqlite:///./bank.db\nENVIRONMENT=production\nJWT_SECRET_KEY=secret\nJWT_ALGORITHM=HS256\n",
    "vercel.json": """{
  "devCommand": "uvicorn src.main:app",
  "builds": [
    {
      "src": "src/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "src/main.py"
    }
  ]
}"""
}

print("🚀 Iniciando o Gerador de Estrutura de Pastas...")

# Loop limpo que apenas escreve os arquivos sem executar o código interno deles
for caminho_arquivo, conteudo_texto in projeto_bancario.items():
    diretorio_pai = os.path.dirname(caminho_arquivo)
    
    if diretorio_pai and not os.path.exists(diretorio_pai):
        os.makedirs(diretorio_pai)
        
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo_fisico:
        arquivo_fisico.write(conteudo_texto)
        
    print(f"✅ Gerado com sucesso: {caminho_arquivo}")

print("\n🎉 Estrutura de TI concluída com sucesso no sistema local!")

