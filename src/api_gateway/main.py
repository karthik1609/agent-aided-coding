from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from backend_loans.services.loan_service import LoanService, bootstrap


class LoanRequest(BaseModel):
    applicant_name: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    income: float = Field(..., gt=0)
    credit_score: int = Field(..., ge=300, le=850)
    existing_debt: float = Field(0, ge=0)


class LoanResponse(BaseModel):
    approved: bool
    rate: float
    reason: str


service = bootstrap()
app = FastAPI(title="Loan Platform API Gateway", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/loans/eligibility", response_model=LoanResponse)
def check_eligibility(request: LoanRequest) -> LoanResponse:
    decision = service.evaluate_application(
        applicant_name=request.applicant_name,
        amount=request.amount,
        income=request.income,
        credit_score=request.credit_score,
        existing_debt=request.existing_debt,
    )

    if decision is None:
        raise HTTPException(status_code=500, detail="Unable to evaluate application")

    return LoanResponse(
        approved=decision.approved,
        rate=decision.offered_rate,
        reason=decision.reason,
    )


def run() -> None:
    import uvicorn

    uvicorn.run("api_gateway.main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    run()
