from sqlalchemy.orm import Session

from . import models, schemas


def get_bill(db: Session, bill_id: int):
    return db.query(models.Bill).filter(models.Bill.id == bill_id).first()


def get_bill_by_code(db: Session, code: str):
    return db.query(models.Bill).filter(models.Bill.code == code).first()


def get_bills(db: Session, skip: int = 0, limit=100):
    return db.query(models.Bill).offset(skip).limit(limit).all()


def create_bill(db: Session, bill: schemas.BillCreate):
    db_bill = models.Bill(
        name=bill.name,
        code=bill.code,
        amount=bill.amount,
        description=bill.description,
        exp_date=bill.exp_date,
        is_paid=bill.is_paid,
    )

    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)

    return db_bill
