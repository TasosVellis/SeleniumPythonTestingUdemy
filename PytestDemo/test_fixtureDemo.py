import pytest

# in fixture we put the name of the fixture in conftest
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo method")
