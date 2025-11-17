import asyncio
from datetime import datetime

from backend_loans.services.loan_service import bootstrap


async def process_fake_feed() -> None:
    service = bootstrap()
    applicants = [
        {"applicant_name": "Casey", "amount": 12000, "income": 65000, "credit_score": 710, "existing_debt": 8000},
        {"applicant_name": "Riley", "amount": 4000, "income": 32000, "credit_score": 610, "existing_debt": 2000},
    ]
    for payload in applicants:
        decision = service.evaluate_application(**payload)
        print(f"[{datetime.utcnow().isoformat()}] Processed {payload['applicant_name']}: {decision.reason}")
        await asyncio.sleep(0.1)


async def worker_loop() -> None:
    while True:
        await process_fake_feed()
        await asyncio.sleep(5)


def main() -> None:
    asyncio.run(worker_loop())


if __name__ == "__main__":
    main()
