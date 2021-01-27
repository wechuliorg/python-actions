from mathlib import add, subract, multiply


def test_additions():
    assert add(1, 2) == 3


def test_subract():
    assert subract(2, 1) == 1


def test_multiply():
    assert multiply(3, 4) == 12
