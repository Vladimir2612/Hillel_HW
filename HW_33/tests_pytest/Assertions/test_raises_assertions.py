import pytest
# Exceptions - https://docs.pytest.org/en/stable/reference/reference.html?highlight=raises#pytest.raises

def test_1():
    with pytest.raises(ZeroDivisionError):
        assert (1 / 0)


def func():
    raise ValueError('Error')


def test_2():
    with pytest.raises(Exception) as exinfo:
        # assert (1, 2, 3) == (1, 2, 4)
        func()
    print(str(exinfo))
    assert str(exinfo.value) == "Error"
