from package_name.source import hi
import pytest


def test_pkg():
    assert True


@pytest.mark.parametrize("tuple1,tuple2", [
    ("2", "10"),
    ("1", "-4"),
])
def test_multiple_things(tuple1, tuple2):
    assert hi(tuple1, tuple2) is True


@pytest.mark.skip(reason="I haven't implemented this in the module yet.")
def test_doesnt_work():
    assert False


@pytest.mark.xfail
def test_div_by_zero():
    assert 1/0 == 1


def test_invalid_input():
    with pytest.raises(TypeError):
        hi("bad input", 3.1415)


def test_something(capture_stdout):
    # This shouldn't go to stdout, because we monkeypatch it.
    # This lets us test the string sent to stdout.
    print("test")
    assert capture_stdout["stdout"] == "test\n"
