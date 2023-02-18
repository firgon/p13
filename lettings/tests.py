import pytest
from django.test import Client
from django.urls import reverse

from lettings.models import Letting
from oc_lettings_site import tests
from oc_lettings_site.tests import convert_to_title


class TestIndex(tests.TestWebPage):
    url = 'lettings_index'
    expected_content = "Lettings"


class TestDetail:
    base_url = 'letting'
    model = Letting
    letting_id = 2

    @pytest.mark.django_db
    def test_page(self):
        client = Client()

        path = reverse(self.base_url,  kwargs={'letting_id': self.letting_id})
        print(path)
        response = client.get(path)
        content = response.content.decode()

        expected_content = convert_to_title(
            self.model.Objects.get(pk=self.letting_id).title)

        assert response.status_code == 200
        assert expected_content in content
