from pickle import _BufferCallback
import pytest, sys

@pytest.fixture(scope="session")
def fixture_thing():
    something = ...
    something_else = ...
    with something as whatever:
        yield whatever

@pytest.fixture
def capture_stdout(monkey_patch):
    buffer = {"stdout":"", "write_calls":0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer
