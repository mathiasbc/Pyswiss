# -*- coding: utf-8 -*-
'''
Not really a pyunit test, just to show how to use the utilities and continually
see their execution
'''

from pyswiss.stack_trace import print_exc_plus


def test_print_exc_plus():
    try:
        print len(3)
    except:
        print_exc_plus()
    assert 1==1

if __name__ == '__main__':
    print("[ * ] Executing test_print_exc_plus test")
    test_print_exc_plus()
