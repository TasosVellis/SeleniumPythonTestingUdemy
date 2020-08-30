# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any method should be wrapped in method


def test_first_program():
    msg = "Hello"
    assert msg == "Hi", "Test failed cause strings don't match"


def test_second_program():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match"
