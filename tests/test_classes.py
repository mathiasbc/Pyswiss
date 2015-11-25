# -*- coding: utf-8 -*-

from pyswiss.classes import AutoParams


def test_autoparams():
    stringvar = 'characters'
    numvar = 7
    parametrized = AutoParams(stringvar=stringvar, numvar=numvar)
    assert 'stringvar' in parametrized.__dict__.keys()
    assert 'numvar' in parametrized.__dict__.keys()
    assert parametrized.stringvar == stringvar
    assert parametrized.numvar == numvar


if __name__ == "__main__":
    pass