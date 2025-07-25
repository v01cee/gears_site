from pydantic import BaseModel
from typing import List, Optional

class RequestForm(BaseModel):
    fio: str
    phone: str
    question: Optional[str] = None
    contacts: List[str] 