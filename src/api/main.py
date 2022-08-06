from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=list[schemas.Bill])
def get_bills(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    bills = crud.get_bills(db, skip=skip, limit=limit)
    return bills


@app.post("/bills/", response_model=schemas.Bill)
def create_bill(bill: schemas.BillCreate, db: Session = Depends(get_db)):
    db_bill = crud.get_bill_by_code(db, code=bill.code)
    if db_bill:
        raise HTTPException(status_code=400, detail="Bill already registered")
    return crud.create_bill(db=db, bill=bill)
