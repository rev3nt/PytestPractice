import pytest


# Прописываем фикстуру, которая будет выполнять "сборку" перед выполнением тестов
@pytest.fixture
def setup():
    # Все, что прописано до yield будет выполнено, перед выполнением функции
    print("setup")
    yield
    # Все, что прописано после будет выполнено после завершения теста
    print("teardown")

# Фикстура, которая выводит сообщение об успешном выполнении модуля тестов
@pytest.fixture(scope="module")
def success_message():
    yield
    print("Tests completed")