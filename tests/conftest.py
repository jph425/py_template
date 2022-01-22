import pytest
import sys


class DB:
    pass


@pytest.fixture(scope="session")
def fixture_thing():
    with DB() as db:
        yield db  # yield ensures teardown code is executed


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer
