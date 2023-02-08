import pytest

cites = ['Dnipro', 'Odesa', 'Kyiv']


@pytest.fixture()
def setup_list():
    cites.append('Lviv')
    yield cites
    print('After fixture')
    cites.pop()


@pytest.fixture()
def setup_list2():
    cites.append('Lviv')
    yield cites
    print('After fixture2')
    cites.pop()


def test_check_items(setup_list):
    print(setup_list)
    assert setup_list[-1] == 'Lviv'


def test_check_items2(setup_list, setup_list2):
    assert len(setup_list) == len(setup_list2)