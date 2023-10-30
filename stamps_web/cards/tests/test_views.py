from datetime import datetime
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from tests.factories.card import CardTypeFactory, CardFactory
from tests.factories.user import UserFactory
from freezegun import freeze_time
from cards.models import CardType, Card
from cards.serializers import CardTypeSerializer, CardSerializer
from tests.factories.companies import CompanyUserFactory
from parameterized import parameterized
import pytz


@freeze_time("2012-01-14")
class TestCardTypeViewSet(TestCase):
    def setUp(self):
        self.company_user = CompanyUserFactory()
        self.user = self.company_user.user
        self.client = APIClient()
        self.user_company = self.company_user.company

        self.card_type = CardTypeFactory(company=self.user_company)

    def test_get_detailed(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f"/api/card_types/{self.card_type.id}/")

        expected_data = {
            "name": self.card_type.name,
            "company_name": self.card_type.company.name,
            "created_by": self.card_type.created_by.username,
            "maximum_stamps": self.card_type.maximum_stamps,
            "created_at": "2012-01-14T00:00:00Z",
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_get_detailed_not_authenticated(self):
        response = self.client.get(f"/api/card_types/{self.card_type.id}/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detailed_not_company_user(self):
        card_type = CardTypeFactory()
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"/api/card_types/{card_type.id}/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list(self):
        """
        Test list - returns only CardTypes of Company User
        """
        CardTypeFactory()
        CardTypeFactory()
        card_type_3 = CardTypeFactory(company=self.user_company)

        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/card_types/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                CardTypeSerializer(instance=self.card_type).data,
                CardTypeSerializer(instance=card_type_3).data,
            ],
        )

    @parameterized.expand(
        [
            (1, "baba"),
            (3, "asdd"),
            (11, "adanos"),
            (19, "innos"),
        ]
    )
    def test_post_create(self, max_stamps, name):
        self.client.force_authenticate(user=self.user)
        data = {
            "name": name,
            "maximum_stamps": max_stamps,
            "company": self.user_company.id,
        }
        response = self.client.post("/api/card_types/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_delete_card_type(self):
        card_type_1 = CardTypeFactory()
        card_type_2 = CardTypeFactory()

        self.client.force_authenticate(user=self.user)

        card_types_all = list(CardType.objects.all())
        self.assertIn(card_type_1, card_types_all)
        self.assertIn(card_type_2, card_types_all)
        self.assertIn(self.card_type, card_types_all)

        response = self.client.delete(f"/api/card_types/{self.card_type.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        card_types_all = list(CardType.objects.all())
        self.assertIn(card_type_1, card_types_all)
        self.assertIn(card_type_2, card_types_all)
        self.assertNotIn(self.card_type, card_types_all)

    @parameterized.expand(
        [
            (1, "baba", 4, "limbo of the lost"),
            (3, "asdd", 19, "doom"),
        ]
    )
    def test_patch_card_type(self, max_stamps, name, changed_max_stamps, changed_name):
        self.card_type.name = name
        self.card_type.maximum_stamps = max_stamps
        self.card_type.save()

        self.client.force_authenticate(user=self.user)
        data = {
            "name": changed_name,
            "maximum_stamps": changed_max_stamps,
        }

        response = self.client.patch(f"/api/card_types/{self.card_type.id}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            dict(response.data),
            {
                "name": changed_name,
                "company_name": self.card_type.company.name,
                "created_by": self.card_type.created_by.username,
                "maximum_stamps": changed_max_stamps,
                "created_at": "2012-01-14T00:00:00Z",
            },
        )

        changed_card_type = CardType.objects.get(id=self.card_type.id)
        self.assertEqual(changed_card_type.name, changed_name)
        self.assertEqual(changed_card_type.maximum_stamps, changed_max_stamps)

    def test_patch_card_type_is_not_company_user(self):
        card_type_user_is_not_allowed = CardTypeFactory()
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "changed_name",
            "maximum_stamps": 123,
        }

        response = self.client.patch(
            f"/api/card_types/{card_type_user_is_not_allowed.id}/", data=data
        )
        # it could be 403 too but it is even better not to show the object exists but user has no access
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_card_type(self):
        """
        test put method is not be allowed
        """
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "changed_name",
            "maximum_stamps": 1,
            "company_name": self.card_type.company.name,
        }
        response = self.client.put(f"/api/card_types/{self.card_type.id}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


@freeze_time("2012-12-21")
class TestCardViewSet(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.card_owned = CardFactory(
            card_owner=self.user,
            expiration_date=datetime(2013, 1, 15, tzinfo=pytz.utc),
        )

    def test_get_detailed(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f"/api/cards/{self.card_owned.id}/")

        expected_data = {
            "id": self.card_owned.id,
            "company_name": self.card_owned.card_type.company.name,
            "company_logo_url": "https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg",
            "company_stamp_url": "http://www.pngall.com/wp-content/uploads/2016/07/Sun-Download-PNG.png",
            "company_background_image_url": None,
            "card_owner": self.user.id,
            "start_date": "2012-12-21T00:00:00Z",
            "expiration_date": "2013-01-15T00:00:00Z",
            "collected_stamps": 0,
            "updated_at": "2012-12-21T00:00:00Z",
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_get_detailed_not_authenticated(self):
        response = self.client.get(f"/api/cards/{self.card_owned.id}/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detailed_not_card_owner(self):
        card_not_owned = CardFactory()
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"/api/cards/{card_not_owned.id}/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_list(self):
        """
        Test list - returns only Cards of the User
        """
        CardFactory()
        CardFactory()
        card_1 = CardFactory(card_owner=self.user)
        card_2 = CardFactory(card_owner=self.user)
        card_3 = CardFactory(card_owner=self.user)

        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/cards/")

        expected_data = [
            {
                "id": self.card_owned.id,
                "company_name": self.card_owned.card_type.company.name,
                "company_logo_url": "https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg",
                "company_stamp_url": "http://www.pngall.com/wp-content/uploads/2016/07/Sun-Download-PNG.png",
                "company_background_image_url": None,
                "card_owner": self.user.id,
                "start_date": "2012-12-21T00:00:00Z",
                "expiration_date": "2013-01-15T00:00:00Z",
                "collected_stamps": 0,
                "updated_at": "2012-12-21T00:00:00Z",
            },
            CardSerializer(instance=card_1).data,
            CardSerializer(instance=card_2).data,
            CardSerializer(instance=card_3).data,
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_delete_card(self):
        card_not_owned = CardFactory()
        card_1 = CardFactory(card_owner=self.user)
        self.client.force_authenticate(user=self.user)

        card_types_all = list(Card.objects.all())
        self.assertIn(card_not_owned, card_types_all)
        self.assertIn(card_1, card_types_all)
        self.assertIn(self.card_owned, card_types_all)

        response = self.client.delete(f"/api/cards/{self.card_owned.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        card_types_all = list(Card.objects.all())
        self.assertIn(card_not_owned, card_types_all)
        self.assertIn(card_1, card_types_all)
        self.assertNotIn(self.card_owned, card_types_all)

    def test_patch_card_not_allowed(self):
        """
        test patch method is not be allowed
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(f"/api/cards/{self.card_owned.id}/", data={})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_card_not_allowed(self):
        """
        test put method is not be allowed
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.put(f"/api/cards/{self.card_owned.id}/", data={})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_card(self):
        self.client.force_authenticate(user=self.user)
        card_type = CardTypeFactory()
        data = {
            "card_type": card_type.id,
        }
        self.assertEqual(1, Card.objects.count())

        response = self.client.post("/api/cards/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
        self.assertEqual(2, Card.objects.count())

    def test_create_card_inject_some_data(self):
        """
        Test create card does not allow to enter other properties
        """
        self.client.force_authenticate(user=self.user)
        card_type = CardTypeFactory()
        data = {
            "card_type": card_type.id,
            "collected_stamps": 15,
        }
        self.assertEqual(1, Card.objects.count())

        response = self.client.post("/api/cards/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(2, Card.objects.count())
        self.assertEqual(response.data, {"card_type": card_type.id})

    def test_increment_card_stamps_is_not_company_user(self):
        """
        Test increment stamps when user is not company user
        """
        self.client.force_authenticate(user=self.user)
        self.assertEqual(0, self.card_owned.collected_stamps)

        response = self.client.patch(f"/api/cards/{self.card_owned.id}/increment/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(0, self.card_owned.collected_stamps)

    def test_increment_card_stamps_ok(self):
        """
        Test increment stamps when user is company user
        """
        company_user = CompanyUserFactory()
        company = company_user.company
        company_card_type = CardTypeFactory(company=company)
        card = CardFactory(card_type=company_card_type, card_owner=self.user)
        self.client.force_authenticate(user=company_user.user)
        self.assertEqual(0, card.collected_stamps)

        response = self.client.patch(f"/api/cards/{card.id}/increment/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        card.refresh_from_db()
        self.assertEqual(1, card.collected_stamps)
        self.assertEqual(response.data, CardSerializer(instance=card).data)

    def test_increment_card_stamps_company_user_not_allowed(self):
        """
        Test increment stamps when user is company user but not card type is others company
        """
        company_user = CompanyUserFactory()
        company_card_type = CardTypeFactory()
        card = CardFactory(card_type=company_card_type, card_owner=self.user)
        self.client.force_authenticate(user=company_user.user)
        self.assertEqual(0, card.collected_stamps)

        response = self.client.patch(f"/api/cards/{card.id}/increment/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        card.refresh_from_db()
        self.assertEqual(0, card.collected_stamps)
