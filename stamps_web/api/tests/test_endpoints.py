from django.http import HttpRequest
from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time
from rest_framework import status
from rest_framework.test import APIClient

from api.endpoints import get_my_cards
from tests.factories.card import CardFactory, CardTypeFactory
from tests.factories.user import UserFactory


@freeze_time("2012-01-14")
class TestGetMyCards(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.card_type = CardTypeFactory()
        self.client = APIClient()

    def test_get_my_cards(self):
        """Test get_my_cards"""
        self.client.force_authenticate(user=self.user)

        card_start_date = timezone.now()
        card = CardFactory(
            start_date=card_start_date,
            card_owner=self.user,
        )
        request = HttpRequest()
        request.user = self.user
        request.method = "GET"
        resp = get_my_cards(request)

        card_start_date = card_start_date.isoformat().split("+")[0]
        expected_data = {
            "company_name": f"{card.company.name}",
            "company_logo_url": "https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg",
            "company_stamp_url": "http://www.pngall.com/wp-content/uploads/2016/07/Sun-Download-PNG.png",
            "company_background_image_url": None,
            "card_owner": 1,
            "start_date": "2012-01-14T00:00:00Z",
            "used_date": None,
            "expiration_date": None,
            "collected_stamps": 0,
        }

        self.assertEqual(dict(resp.data[0]), expected_data)

    def test_get_my_cards_no_user(self):
        """Test get_my_cards no user"""
        request = HttpRequest()
        request.method = "GET"
        resp = get_my_cards(request)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, resp.status_code)
