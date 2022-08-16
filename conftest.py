# push_задание7
import pytest
from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.dectroy)
    return fixture
