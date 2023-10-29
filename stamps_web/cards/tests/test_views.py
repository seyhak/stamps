from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from tests.factories.card import CardTypeFactory
from tests.factories.user import UserFactory
from freezegun import freeze_time
from cards.models import CardType
from cards.serializers import CardTypeSerializer
from tests.factories.companies import CompanyFactory
from parameterized import parameterized


@freeze_time("2012-01-14")
class TestCardTypeViewSet(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.user_company = CompanyFactory()
        self.user.company = self.user_company
        self.user.save()
        self.card_type = CardTypeFactory(company=self.user_company)

    def test_get_detailed(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f"/api/card_type/{self.card_type.id}/")

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
        response = self.client.get(f"/api/card_type/{self.card_type.id}/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detailed_not_company_user(self):
        card_type = CardTypeFactory()
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"/api/card_type/{card_type.id}/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_list(self):
        """
        Test list - returns only CardTypes of Company User
        """
        CardTypeFactory()
        CardTypeFactory()
        card_type_3 = CardTypeFactory(company=self.user_company)

        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/card_type/")

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
        response = self.client.post("/api/card_type/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_delete_create(self):
        card_type_1 = CardTypeFactory()
        card_type_2 = CardTypeFactory()

        self.client.force_authenticate(user=self.user)

        card_types_all = list(CardType.objects.all())
        self.assertIn(card_type_1, card_types_all)
        self.assertIn(card_type_2, card_types_all)
        self.assertIn(self.card_type, card_types_all)

        response = self.client.delete(f"/api/card_type/{self.card_type.id}/")

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

        response = self.client.patch(f"/api/card_type/{self.card_type.id}/", data=data)
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
            f"/api/card_type/{card_type_user_is_not_allowed.id}/", data=data
        )
        # it could be 403 too but it is even better not to show the object exists but user has no access
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

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
        response = self.client.put(f"/api/card_type/{self.card_type.id}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
