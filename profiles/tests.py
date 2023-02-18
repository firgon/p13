import pytest
from django.contrib.auth.models import User
# from django.test import Client
from django.urls import reverse

from oc_lettings_site import tests
from oc_lettings_site.tests import convert_to_title

from .models import Profile


class TestIndex(tests.TestWebPage):
    url = 'profiles_index'
    expected_content = "Profiles"


class TestDetail:
    base_url = 'profile'
    model = Profile
    letting_id = 2

    @pytest.mark.django_db
    def test_page(self, client):
        user = User.objects.create(username="test")
        profile = Profile.objects.create(user=user, favorite_city="Grenoble")

        path = reverse(self.base_url,
                       kwargs={'username': profile.user.username})
        response = client.get(path)
        content = response.content.decode()

        expected_content = convert_to_title(
            profile.user.username)

        assert response.status_code == 200
        assert expected_content in content
