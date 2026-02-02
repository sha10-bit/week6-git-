# test_app.py
from app import some_function  # if you have functions in app.py

def test_addition():
    assert 2 + 3 == 5

def test_failure():
    assert 1 + 1 == 3  # This will fail and break CI

