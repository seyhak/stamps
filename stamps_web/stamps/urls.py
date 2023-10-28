from django.urls import path

from stamps.views import HomeView
# namespace
app_name = 'stamps'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
