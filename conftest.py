# -*- coding: utf-8 -*-
import pytest
from fixture.application import Aplication

@pytest.fixture(scope="session")
def app(request):
    fixture = Aplication()
    #fixture.session.login(email="a@redmadrobot.com", password="swordfish42_is_bad_password_you_know!!!")
    request.addfinalizer(fixture.destroy)
    return fixture