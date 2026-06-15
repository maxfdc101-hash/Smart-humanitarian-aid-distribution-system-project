
from pydantic import BaseModel, Field
from typing import Literal



HousingType = Literal[
    "مدمر بالكامل",
    "مدمر جزئيا",
    "ايجار",
    "مخيم ايواء/خيمة"
]

class FamilyData(BaseModel):
    SpecialCase: bool = Field(
    ...,
    description="هل توجد حالة خاصة؟ true أو false"
)
    Income: float = Field(..., ge=0)
    FamilyMembers: int = Field(..., ge=1)
    Housing: HousingType = Field(..., description="نوع السكن")





class PredictionResponse(BaseModel):
    PriorityScore: float
    PriorityLevel: str

