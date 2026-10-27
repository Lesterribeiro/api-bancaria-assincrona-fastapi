from fastapi import APIRouter, HTTPException, status

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
