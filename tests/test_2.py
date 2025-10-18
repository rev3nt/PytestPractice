import pytest


@pytest.fixture
def setup():
    print("setup")
    # yield также позволяет не только выполнять действия после теста, но и возвращает значение
    yield 52
    print("teardown")


# Просто тесты, которые выполнятся без каких-либо дополнительных действий до или после
def test_email(setup):
    print(f"test_email, and value: {setup}")


# Просто тесты, которые выполнятся без каких-либо дополнительных действий до или после
def test_login():
    print("test_login")