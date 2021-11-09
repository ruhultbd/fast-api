from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    is_active: Optional[bool]=True
