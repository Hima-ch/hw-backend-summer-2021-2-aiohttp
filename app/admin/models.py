from dataclasses import dataclass

from app.quiz.models import Answer


@dataclass
class Admin:
    id: int
    email: str
    password: str | None = None

