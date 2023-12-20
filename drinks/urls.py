from . import views
from django.urls import path

urlpatterns = [
    path('', views.drink_list),
    path('<int:pk>/', views.drink_detail),
]