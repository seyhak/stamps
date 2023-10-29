from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.endpoints import get_my_cards
from cards import views as cards_views

router = DefaultRouter()
router.register(r'card_type', cards_views.CardTypeViewSet, basename="card_type")

urlpatterns = [
    path('', include(router.urls)),
    path('get_my_cards/', get_my_cards),
]
