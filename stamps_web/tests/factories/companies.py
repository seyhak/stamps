from factory.django import DjangoModelFactory

from companies.models import Company, CompanyUser
from factory import fuzzy, SubFactory
from tests.factories.user import UserFactory


class CompanyFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12)

    class Meta:
        model = Company


class CompanyUserFactory(DjangoModelFactory):
    company = SubFactory(CompanyFactory)
    user = SubFactory(UserFactory)

    class Meta:
        model = CompanyUser

