from django.core.exceptions import ObjectDoesNotExist
from rest_framework import (decorators, exceptions, mixins, permissions,
                            status, viewsets)
from rest_framework.response import Response

from cards.models import Card, CardType

from .permissions import (IsAllowedToIncrementStamps, IsCardOwner,
                          IsCompanysUserCardType)
from .serializers import (CardCreateSerializer, CardSerializer,
                          CardTypeCreateSerializer, CardTypeSerializer)


class CardTypeViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        "create": CardTypeCreateSerializer,
    }
    queryset = CardType.objects.all()
    default_serializer_class = CardTypeSerializer
    permission_classes = [
        permissions.IsAdminUser | IsCompanysUserCardType,
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        if self.action == "list":
            try:
                company = self.request.user.companyuser.company
            except ObjectDoesNotExist:
                raise exceptions.PermissionDenied("User is not company user")
            return self.queryset.filter(company=company)
        return super().get_queryset()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        if self.action == "update":
            response = {"message": "Update function is not offered in this path."}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)


class CardViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.ReadOnlyModelViewSet
):
    INCREMENT_STAMPS_AMOUNT_ACTION = "increment_stamps_amount"
    serializer_classes = {
        "create": CardCreateSerializer,
    }
    queryset = Card.objects.all()
    default_serializer_class = CardSerializer
    permission_classes = [
        permissions.IsAdminUser | IsCardOwner,
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        user = self.request.user
        if self.action == self.INCREMENT_STAMPS_AMOUNT_ACTION:
            return self.queryset
        return self.queryset.filter(card_owner=user)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @decorators.action(
        detail=True,
        methods=["patch"],
        url_path="increment",
        permission_classes=[IsAllowedToIncrementStamps, permissions.IsAuthenticated],
        queryset=Card.objects.all(),
    )
    def increment_stamps_amount(self, request, pk=None):
        card = self.get_object()
        card.collected_stamps += 1
        card.save()
        return Response(CardSerializer(instance=card).data, status=status.HTTP_200_OK)
