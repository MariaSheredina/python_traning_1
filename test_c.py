import pytest
from contact import Contact
from application_contact import Application_contact

@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.dectroy)
    return fixture

def test_contact (app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Maria", middlename="Victorovna", lastname="Sidorova", nickname="Mari", company="Company", address="NNovgorod", mobile="9200150025", bday="4", bmonth="12", byear="1981"))
    app.logout()
