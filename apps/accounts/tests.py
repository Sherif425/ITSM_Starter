import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_list_requires_auth():
    client = APIClient()
    url = reverse('user-list')
    resp = client.get(url)
    assert resp.status_code in (401, 403)
