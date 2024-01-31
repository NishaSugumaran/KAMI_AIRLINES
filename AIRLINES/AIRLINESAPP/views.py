
# Create your views here.
from rest_framework import  viewsets
from .serializer import AirplaneSerializer
from .models import AirplaneInfo
from rest_framework.response import Response
from rest_framework import status
from typing import Any
from rest_framework.request import Request

#Class view for handling CRUD operations
class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = AirplaneInfo.objects.all()
    serializer_class = AirplaneSerializer
    
    #Overriding create method to handle multiple inputs on single POST request
    def create(self, request, *args, **kwargs): 
        # type: (Request, *Any, **Any) -> Response
        data=request.data
        many = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
        )

