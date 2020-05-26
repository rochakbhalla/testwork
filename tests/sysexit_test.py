#pytest -x           # stop after first failure
#pytest --maxfail=2  # stop after two failures

import pytest

def f():
    raise SystemError(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()