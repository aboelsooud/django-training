import pytest

from rest_framework.test import APIClient
from knox.auth import AuthToken
from users.models import User

@pytest.fixture
def auth_client(user = None):
    def _auth_client(user = None):
        if user == None:
            user = User.objects.create_user(username = "random", email = "random@mail.com", password = "Random1_")
    
        _, token = AuthToken.objects.create(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        return client
    
    return _auth_client