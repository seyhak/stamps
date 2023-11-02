from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from api.endpoints import get_my_cards
from cards import views as cards_views

router = DefaultRouter()
router.register(r"card_types", cards_views.CardTypeViewSet, basename="card_type")
router.register(r"cards", cards_views.CardViewSet, basename="card")

urlpatterns = [
    path("", include(router.urls)),
    # path('get_my_cards/', get_my_cards),  # legacy code
]
