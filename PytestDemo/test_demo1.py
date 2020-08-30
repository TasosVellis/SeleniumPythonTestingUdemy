# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any method should be wrapped in method
# Method name should make sense
# -k stands for method names execution, -s logs in output - v stands for metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
