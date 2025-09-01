from sqlalchemy.orm import Session
from . import models, schemas

# Get all FAQs
def get_faqs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FAQ).offset(skip).limit(limit).all()

# Create a new FAQ
def create_faq(db: Session, faq: schemas.FAQCreate):
    db_faq = models.FAQ(question=faq.question, answer=faq.answer)
    db.add(db_faq)
    db.commit()
    db.refresh(db_faq)
    return db_faq

# Optional: get FAQ by ID
def get_faq(db: Session, faq_id: int):
    return db.query(models.FAQ).filter(models.FAQ.id == faq_id).first()
