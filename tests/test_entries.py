import pytest
from pydantic import ValidationError

from blackboard.entries import Entry, Goal, Note


def test_goal_has_its_type_and_fields() -> None:
    g = Goal(question="why?")
    assert g.type == "goal"
    assert g.question == "why?"
    assert g.author == "user"


def test_goal_requires_a_question() -> None:
    with pytest.raises(ValidationError):
        Goal()  # type: ignore[call-arg]


def test_every_entry_gets_its_own_id_and_timestamp() -> None:
    a, b = Note(text="a"), Note(text="b")
    assert a.id != b.id
    assert a.timestamp.tzinfo is not None  # timezone-aware


def test_entries_are_immutable() -> None:
    g = Goal(question="why?")
    with pytest.raises(ValidationError):
        g.question = "changed"  # type: ignore[misc]


def test_tags_default_to_empty() -> None:
    assert Note(text="x").tags == frozenset()


def test_summary_is_one_line_description() -> None:
    assert Goal(question="why?").summary() == "why?"
    assert Note(text="hi").summary() == "hi"
    assert Entry(type="raw").summary() == ""
