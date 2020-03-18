

from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions , generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer , IncomeSerializer

from accounts.models import Incomes
from datetime import datetime



class CustomAuthToken(ObtainAuthToken):
    def post(self , request , *args , **kwargs):
        serializer = self.serializer_class(data = request.data, context = {'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user = user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class Test(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self , request):
        user = request.user
        return Response({
            'Resonse': user.username
        })

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Incomes.objects.all()
    class Meta:
        model = Incomes
        fields= ['name' , 'place']
    

    
# Create your views here.

