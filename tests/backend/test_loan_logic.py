from backend_loans.services.loan_service import LoanService
from backend_loans.repositories.repository import InMemoryLoanRepository


def test_evaluate_application_approves_low_ratio() -> None:
    repo = InMemoryLoanRepository()
    service = LoanService(repo)

    decision = service.evaluate_application(
        applicant_name="Alex",
        amount=5000,
        income=85000,
        credit_score=730,
        existing_debt=2000,
    )

    assert decision is not None
    assert decision.approved is True
    assert decision.offered_rate > 0


def test_evaluate_application_declines_high_ratio() -> None:
    repo = InMemoryLoanRepository()
    service = LoanService(repo)

    decision = service.evaluate_application(
        applicant_name="Sam",
        amount=20000,
        income=40000,
        credit_score=600,
        existing_debt=15000,
    )

    assert decision is not None
    assert decision.approved is False
