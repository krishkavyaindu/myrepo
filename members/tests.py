from django.test import TestCase
from django.urls import reverse

def test_index_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'Welcome to My Django App' in str(response.content)

