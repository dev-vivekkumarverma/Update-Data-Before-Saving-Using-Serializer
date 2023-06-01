from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Alarm
from rest_framework import status
from .serializer import AlarmSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(["POST","GET"])
def create_alarm(request):
    try:
        if request.method=="POST":
            print("request.data:",request.data)
            deserialized_data=AlarmSerializer(data=request.data)
            if deserialized_data.is_valid():
                deserialized_data.save()
                print(deserialized_data.data)
                return Response(data=deserialized_data.data,status=status.HTTP_201_CREATED)
            else:
                raise Exception("some fields missing")
        elif request.method=="GET":
            alarm_objects=Alarm.objects.all()
            serialized_data=AlarmSerializer(alarm_objects,many=True)
            return Response(data=serialized_data.data,status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)