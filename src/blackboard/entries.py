"""Typed board entries. New entry types go in this file."""

from datetime import UTC, datetime
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


def _new_id() -> str:
    return str(uuid4())


def _now() -> datetime:
    return datetime.now(UTC)


class Entry(BaseModel):
    """One fact on the board. Once posted, it never changes."""

    model_config = ConfigDict(frozen=True)

    id: str = Field(default_factory=_new_id)
    type: str
    author: str = "user"
    tags: frozenset[str] = frozenset()
    timestamp: datetime = Field(default_factory=_now)
    round: int = 0
    caused_by: tuple[str, ...] = ()

    def summary(self) -> str:
        return ""


class Note(Entry):
    type: Literal["note"] = "note"
    text: str = ""

    def summary(self) -> str:
        return self.text


class Goal(Entry):
    # Accepts specific literal values
    type: Literal["goal"] = "goal"
    question: str

    def summary(self) -> str:
        return self.question
