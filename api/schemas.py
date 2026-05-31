
from pydantic import BaseModel, Field


class FamilyData(BaseModel):
    SpecialCase: int = Field(..., ge=0, le=1)
    Income: float = Field(..., ge=0)
    FamilyMembers: int = Field(..., ge=1)
    Housing: int


class PredictionResponse(BaseModel):
    PriorityScore: float
    PriorityLevel: str

