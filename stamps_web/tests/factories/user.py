from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from factory import fuzzy


class UserFactory(DjangoModelFactory):
    username = fuzzy.FuzzyText(length=12)

    class Meta:
        model = User
