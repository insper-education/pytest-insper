import pytest


def test_always_pass():
    assert True


@pytest.mark.dependency_level(0)
def test_level0():
    assert True


@pytest.mark.dependency_level(1)
def test_level1():
    assert True


@pytest.mark.dependency_level(0)
def test_other_level0():
    assert False