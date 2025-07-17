from pydantic import BaseModel
from typing import List, Optional

class CatBreed(BaseModel):
    id: str
    name: str
    origin: Optional[str]
    description: Optional[str]
    temperament: Optional[str]
