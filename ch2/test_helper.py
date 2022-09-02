import pytest
from cards import Card


def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True
    assert c1 == c2
    if c1.id != c2.id:
        pytest.fail(f"id's don't mutch {c1.id} != {c2.id}")

def test_identical():
    c1 = Card('foo', id=1)
    c2 = Card('foo', id=1)
    assert_identical(c1, c2)

def test_indentical_fail():
    c1 = Card('foo', id=1)
    c2 = Card('foo', id=2)
    assert_identical(c1, c2)
