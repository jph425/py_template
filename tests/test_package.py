from package_name import symbol
import pytest

def test_pkg():
    assert True

@pytest.mark.parametrize("tuple1,tuple2", [
    ("a", "b"),
    ("c", "d"),
])
def test_multiple_things(tuple1, tuple2):
    assert func(tuple1) is tuple2

@pytest.mark.skip(reason="I haven't implemented this in the module yet.")
def test_whoops():
    assert False

@pytest.mark.xfail
def test_ill_get_this():
    assert 1/0 == 1

def test_invalid_input():
    with pytest.raises(ValueError):
        func("bad input")

def test_something(fixture_thing):
    func(fixture_thing)
    assert ...
