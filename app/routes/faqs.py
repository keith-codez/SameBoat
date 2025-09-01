from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db
from ..services.ai import generate_response


router = APIRouter(
    prefix="/faqs",
    tags=["FAQs"]
)

# POST a new FAQ
@router.post("/", response_model=schemas.FAQResponse)
def create_faq(faq: schemas.FAQCreate, db: Session = Depends(get_db)):
    db_faq = crud.create_faq(db, faq)

    ai_output = generate_response(faq.question, faq.answer)
    db_faq.ai_response = ai_output
    db.commit()
    db.refresh(db_faq)

    return db_faq



@router.get("/", response_model=list[schemas.FAQResponse])
def get_faqs(db: Session = Depends(get_db)):
    return crud.get_faqs(db)

    
# Optional: GET FAQ by ID

@router.get("/{faq_id}", response_model=schemas.FAQResponse)
def read_faq(faq_id: int, db: Session = Depends(get_db)):
    db_faq = crud.get_faq(db, faq_id)
    if not db_faq:
        raise HTTPException(status_code=404, detail="FAQ not found")
    return db_faq

