from django.shortcuts import render
from rest_framework import request, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import *

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly 
from rest_framework.authtoken.models import Token


#### import serializers
from .serializers import *

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        #print(token)
        return Response({
                'token': token.key, 
                }, 
            status=status.HTTP_201_CREATED)
    #def list(self, request, *args, **kwargs):
    #    response = {'message': 'You cant create rating like that'}
    #    return Response(response, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated ,)
    
    #print(request.user)
    