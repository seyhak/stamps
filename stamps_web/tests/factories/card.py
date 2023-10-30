from factory import fuzzy, SubFactory
from factory.django import DjangoModelFactory

from cards.models import Card, CardType
from tests.factories.companies import CompanyFactory
from tests.factories.user import UserFactory


class CardTypeFactory(DjangoModelFactory):
    class Meta:
        model = CardType

    name = fuzzy.FuzzyText(length=12)
    company = SubFactory(CompanyFactory)
    maximum_stamps = fuzzy.FuzzyInteger(1, 20)
    created_by = SubFactory(UserFactory)


class CardFactory(DjangoModelFactory):
    class Meta:
        model = Card

    card_owner = SubFactory(UserFactory)
    card_type = SubFactory(CardTypeFactory)
