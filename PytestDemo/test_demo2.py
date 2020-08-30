# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any method should be wrapped in method
# Method name should make sense
# -k stands for method names execution, -s logs in output - v stands for metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# fixtures are used as setup and tear down methods for test cases
# -conftest file to generalize fixture and make it available to all test cases(fixture name into parameters of method)
# datadriver and parameterazition can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end


import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_first_program():
    msg = "Hello"  # operations
    assert msg == "Hi", "Test failed cause strings don't match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match"

# Fixtures are like prerequisites
