from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response

from .models import Drink
from .serializers import DrinkSerializer
# Create your views here.

def drink_list(request):
    # get all the drinks from the database
    all_drinks = Drink.objects.all()
    # serialize them into json
    serializer = DrinkSerializer(all_drinks, many=True)
    # return the json as  response
    return JsonResponse({'drinks':serializer.data})
