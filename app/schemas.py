from pydantic import BaseModel
from datetime import datetime

class FAQBase(BaseModel):
    question: str
    answer: str

class FAQCreate(FAQBase):
    question: str
    answer: str

class FAQ(FAQBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True  # Pydantic v2
    }

class FAQOut(FAQBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}

class FAQResponse(FAQCreate):
    id: int
    ai_response: str | None = None
    created_at: datetime

    class Config:
        orm_mode = True

        
# --------- BLOGS ---------
class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}

class BlogResponse(BlogBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
