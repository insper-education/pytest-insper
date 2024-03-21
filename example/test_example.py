import pytest
from pytest_insper.assertions import assert_code_quality


def test_always_pass():
    assert True


@pytest.mark.dependency_level(0)
def test_level0():
    assert True


@pytest.mark.dependency_level(1)
def test_level1():
    assert True


@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (4, 5, 9), (10, 11, 12), (13, 14, 15)])
@pytest.mark.dependency_level(0)
@pytest.mark.max_points(16)
def test_other_level0(a, b, c):
    assert a + 1 == b and b + 1 == c


def test_code_quality():
    a = 10
    a = a
    assert_code_quality(['pltest.py'])
