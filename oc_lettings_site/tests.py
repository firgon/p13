import pytest
from django.test import Client
from django.urls import reverse


def convert_to_title(title: str)-> str:
    return f"<h1>{title}</h1>"


class TestWebPage:
    url = 'index'
    expected_content = "Welcome to Holiday Homes"

    @pytest.mark.django_db
    def test_page(self, client):

        path = reverse(self.url)
        response = client.get(path)
        content = response.content.decode()
        assert response.status_code == 200
        assert convert_to_title(self.expected_content) in content

