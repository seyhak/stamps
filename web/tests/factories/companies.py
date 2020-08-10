from factory.django import DjangoModelFactory

from companies.models import Company


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company
