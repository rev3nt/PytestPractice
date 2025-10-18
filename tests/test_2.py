# Просто тесты, которые выполнятся без каких-либо дополнительных действий до или после
def test_email(setup):
    print(f"test_email, and value: {setup}")


# Просто тесты, которые выполнятся без каких-либо дополнительных действий до или после
def test_login(success_message):
    print("test_login")