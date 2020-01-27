
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions , generics
from knox.models import AuthToken
from rest_framework import serializers
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer , IncomeSerializer


# Create your views here.

@permission_classes((permissions.AllowAny,))
class user_authenticate(APIView):
    def get(self, request):
        content = {'message':'hello world'}
        return Response(content)

    def post(self , request):
        print(request.body)
        content = {'message': 'hello world'}
        return Response(content)

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self , request , *args , **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        print(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class IncomeAPIView(generics.GenericAPIView):
    serializer_class = IncomeSerializer

    def post(self , request):
        return Response({
            "success": "success"
        })
        