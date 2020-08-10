from django.http import HttpRequest
from django.test import TestCase
from django.utils import timezone

from api.endpoints import get_my_cards
from tests.factories.card import CardFactory
from tests.factories.user import UserFactory


class TestGetMyCars(TestCase):
    def test_get_my_cards(self):
        """Test get_my_cards"""
        user = UserFactory()
        card_start_date = timezone.now()
        CardFactory(
            start_date=card_start_date,
            maximum_stamps=20,
            user=user,
        )
        request = HttpRequest()
        request.USER = user
        request.method = 'GET'
        resp = get_my_cards(request)

        card_start_date = card_start_date.isoformat().split('+')[0]
        expected_data = [{
            'collected_stamps': 0,
            'company_logo_url': 'https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg',
            'expiration_date': None,
            'maximum_stamps': 20,
            'start_date': f'{card_start_date}Z',
            'used_date': None,
            'user': 1
        }]
        self.assertJSONEqual(
            resp.data,
            expected_data
        )

    def test_get_my_cards_no_user(self):
        """Test get_my_cards no user"""
        request = HttpRequest()
        request.method = 'GET'
        resp = get_my_cards(request)
        self.assertEqual(401, resp.status_code)
