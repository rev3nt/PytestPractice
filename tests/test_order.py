import pytest

# Добавляем декоратор, который задаем очередность выполнения теста, в данном случае тест выполнится вторым
@pytest.mark.run(order=2)
def test_method_1(setup):
    print("Method 1")


@pytest.mark.run(order=4)
def test_method_2(setup):
    print("Method 2")


@pytest.mark.run(order=6)
def test_method_3(setup):
    print("Method 3")


@pytest.mark.run(order=1)
def test_method_4(setup):
    print("Method 4")


@pytest.mark.run(order=3)
def test_method_5(setup):
    print("Method 5")


@pytest.mark.run(order=5)
def test_method_6(setup):
    print("Method 6")