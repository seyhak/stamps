from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.endpoints import get_my_cards

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('get_my_cards/', get_my_cards),
]
