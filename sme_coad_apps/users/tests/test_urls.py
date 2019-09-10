import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_redirect(client):
    response = client.get('/usuarios/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_redirect_authenticated(authencticated_client):
    response = authencticated_client.get('/usuarios/')
    assert response.status_code == status.HTTP_200_OK
