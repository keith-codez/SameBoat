from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import crud
from ..database import get_db
from ..services.gpt_writer import generate_blog
from pathlib import Path
from docx import Document

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("/generate/{faq_id}")
def create_blog(faq_id: int, db: Session = Depends(get_db)):
    faq = crud.get_faq(db, faq_id)
    if not faq:
        raise HTTPException(status_code=404, detail="FAQ not found")

    # Generate blog content (with references included in the prompt)
    blog_content = generate_blog(faq.question, faq.answer)

    # Create Word doc
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    slug = faq.question.lower().replace(" ", "-")

    doc = Document()
    doc.add_heading(faq.question, level=1)
    doc.add_paragraph(blog_content)

    # Save as .docx instead of markdown
    file_path = output_dir / f"{slug}.docx"
    doc.save(file_path)

    return {"message": "Blog generated successfully", "file": str(file_path)}
