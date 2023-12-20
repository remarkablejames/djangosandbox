from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Drink
from .serializers import DrinkSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        # get all the drinks from the database
        all_drinks = Drink.objects.all()
        # serialize them into json
        serializer = DrinkSerializer(all_drinks, many=True)
        # return the json as  response
        return JsonResponse({'drinks':serializer.data})
    elif request.method == 'POST':
        pass
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

