from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from backend_loans.domain.models import LoanApplication, LoanDecision


class LoanRepository(ABC):
    """Repository interface for persistence of loan applications and decisions."""

    @abstractmethod
    def save_application(self, application: LoanApplication) -> None: ...

    @abstractmethod
    def save_decision(self, application: LoanApplication, decision: LoanDecision) -> None: ...

    @abstractmethod
    def list_applications(self) -> Iterable[LoanApplication]: ...

    @abstractmethod
    def list_decisions(self) -> Iterable[LoanDecision]: ...


def create_in_memory() -> "InMemoryLoanRepository":
    return InMemoryLoanRepository()


class InMemoryLoanRepository(LoanRepository):
    def __init__(self) -> None:
        self._applications: list[LoanApplication] = []
        self._decisions: list[LoanDecision] = []

    def save_application(self, application: LoanApplication) -> None:
        self._applications.append(application)

    def save_decision(self, application: LoanApplication, decision: LoanDecision) -> None:
        self._decisions.append(decision)

    def list_applications(self) -> Iterable[LoanApplication]:
        return tuple(self._applications)

    def list_decisions(self) -> Iterable[LoanDecision]:
        return tuple(self._decisions)
