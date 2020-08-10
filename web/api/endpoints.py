import json

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
        user = request.USER
    except AttributeError:
        return Response(CardSerializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        cards = Card.objects.filter(user=user)
        serializer = CardSerializer(cards, many=True)
        return Response(json.dumps(serializer.data))

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
