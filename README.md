Pyswiss
========
A collection of python tools with cool insights of the language and useful shortcuts.

Installing:

    $ pip install pyswiss

Examples:

AutoParams:
-----------

```python
from pyswiss.classes import AutoParams


stringvar = 'characters'
numvar = 7
parametrized = AutoParams(stringvar=stringvar, numvar=numvar)
assert 'stringvar' in parametrized.__dict__.keys()
assert 'numvar' in parametrized.__dict__.keys()
```

Traceback:
----------

```python
from pyswiss.stack_trace import print_exc_plus

try:
    print len(3)
except:
    print_exc_plus()
assert 1==1
```

Run the tests:

    $ py.test