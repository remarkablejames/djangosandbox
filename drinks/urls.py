from .views import drink_list
from django.urls import path

urlpatterns = [
    path('', drink_list),
]