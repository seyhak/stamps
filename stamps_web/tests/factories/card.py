from factory import fuzzy, SubFactory
from factory.django import DjangoModelFactory

from cards.models import Card
from tests.factories.companies import CompanyFactory
from tests.factories.user import UserFactory


class CardFactory(DjangoModelFactory):
    class Meta:
        model = Card

    company = SubFactory(CompanyFactory)
    user = SubFactory(UserFactory)
    maximum_stamps = fuzzy.FuzzyInteger(1, 20)
