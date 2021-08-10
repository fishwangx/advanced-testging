from hello import add

from multi import multiply


def test_add():


    assert add(2,3)==5

    assert add(6,7)==13


def test_multi():

    assert multiply(2,3)==6