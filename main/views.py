from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Order


# Create your views here.

class MainView(APIView):
    def get(self, request):
        return Response({'OK?': 'OK'})


class OrderView(APIView):
    def get(self, request):
        order_obj = Order.objects.get(importance='очень срочно')
        return Response(model_to_dict(order_obj))

    def post(self, request):
        order_obj = Order.objects.get(id=1)
        if request.data:
            order_obj = request.data['count']
        else:
            order_obj.count += 1
        order_obj.save()

        return Response(model_to_dict(order_obj))


