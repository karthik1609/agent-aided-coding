from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field


class LoanApplication(BaseModel, frozen=True):
    applicant_name: str
    amount: float = Field(..., gt=0)
    income: float = Field(..., gt=0)
    credit_score: int = Field(..., ge=300, le=850)
    existing_debt: float = Field(0, ge=0)
    submitted_at: datetime = Field(default_factory=datetime.utcnow)


class LoanDecision(BaseModel, frozen=True):
    approved: bool
    offered_rate: float
    reason: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
