import pytest

# if we want to yield at the end of the test we need to define the scope


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Tasos", "Vellis", "tasos.com"]


@pytest.fixture(params=[("chrome", "Tasos", "Vellis"), ("Firefox", "Vellis"), ("IE", "TV")])
def crossBrowser(request):
    return request.param
