from rest_framework.response import Response
from rest_framework import permissions, viewsets, status

from cards.models import CardType
from .permissions import IsCompanysUser
from .serializers import CardTypeSerializer, CardTypeCreateSerializer


class CardTypeViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        'create': CardTypeCreateSerializer,
    }
    queryset = CardType.objects.all()
    default_serializer_class = CardTypeSerializer
    permission_classes = [permissions.IsAdminUser | IsCompanysUser, permissions.IsAuthenticated]

    def get_queryset(self):
        user_company = self.request.user.company
        return self.queryset.filter(company=user_company)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        if self.action == "update":
            response = {'message': 'Update function is not offered in this path.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
