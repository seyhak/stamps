from factory.django import DjangoModelFactory

from companies.models import Company
from factory import fuzzy

class CompanyFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=12)

    class Meta:
        model = Company
