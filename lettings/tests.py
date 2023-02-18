import pytest
from django.urls import reverse

from lettings.models import Letting, Address
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
    def test_page(self, client):
        address = Address.objects.create(number=12, street="rue de la paix",
                                         city="Grenoble", state="France",
                                         zip_code=38000, country_iso_code="FR")
        letting = Letting.objects.create(title="Petit coin de paradis",
                                         address=address)

        path = reverse(self.base_url,  kwargs={'letting_id': letting.id})
        print(path)
        response = client.get(path)
        content = response.content.decode()

        expected_content = convert_to_title(letting.title)

        assert response.status_code == 200
        assert expected_content in content
