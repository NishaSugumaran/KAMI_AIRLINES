from django.shortcuts import render

# Create your views here.
#from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from .serializer import AirplaneSerializer
from .models import AirplaneInfo
from rest_framework.response import Response
from rest_framework import status

class AirplaneViewSet(viewsets.ModelViewSet):
    print("Inside viewset")
    queryset = AirplaneInfo.objects.all()
    serializer_class = AirplaneSerializer
    
    def create(self, request, *args, **kwargs):
        print("Inside create)")
        #data = request.data.get('items', request.data)
        data=request.data
        many = isinstance(data, list)
        print (data, many)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
        )
'''
@api_view(['GET', 'POST'])
def airplane_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        airplane = Airplane.objects.all()
        serializer = AirplaneSerializer(airplane, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AirplaneSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''