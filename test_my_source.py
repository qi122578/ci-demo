import pytest
from my_source import add_func


def test_add_one():
    assert add_func(2, 5) == 7


@pytest.mark.xfail
# 预期为失败的标志
def test_add_fail():
    assert add_func(5, 5) == 1