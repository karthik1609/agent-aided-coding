from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from backend_loans.domain.models import LoanApplication, LoanDecision
from backend_loans.repositories.repository import LoanRepository, create_in_memory


@dataclass(frozen=True)
class EligibilityInputs:
    amount: float
    income: float
    credit_score: int
    existing_debt: float


class LoanService:
    def __init__(self, repository: LoanRepository) -> None:
        self.repository = repository

    def evaluate_application(
        self,
        applicant_name: str,
        amount: float,
        income: float,
        credit_score: int,
        existing_debt: float = 0,
    ) -> Optional[LoanDecision]:
        application = LoanApplication(
            applicant_name=applicant_name,
            amount=amount,
            income=income,
            credit_score=credit_score,
            existing_debt=existing_debt,
        )
        self.repository.save_application(application)

        ratio = (existing_debt + amount) / max(income, 1)
        adjusted_score = credit_score - (ratio * 100)

        approved = adjusted_score >= 620 and ratio <= 0.45
        base_rate = 0.05
        risk_premium = max(0, (700 - adjusted_score) / 2000)
        offered_rate = round(base_rate + risk_premium, 4)

        reason = "Approved" if approved else "Debt-to-income ratio too high or credit score too low"
        decision = LoanDecision(approved=approved, offered_rate=offered_rate, reason=reason)
        self.repository.save_decision(application, decision)
        return decision

    def list_recent_decisions(self) -> list[LoanDecision]:
        return list(self.repository.list_decisions())


_def_repository = create_in_memory()

def bootstrap(repository: LoanRepository | None = None) -> LoanService:
    return LoanService(repository or _def_repository)
