from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cards.models import Card
from cards.serializers import CardSerializer


@api_view(['GET', 'POST'])
def get_my_cards(request):
    try:
        user = request.user
    except AttributeError:
        user = True

    if user.is_anonymous:
        return Response(CardSerializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        cards = Card.objects.filter(user=user)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
