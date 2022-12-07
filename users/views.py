from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response


# view for registering users
class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class RegisterView(APIView):
#
#     def post(self, request):
#         username = request.data['username',]
#         password = request.data['password',]
#         user = User(username=username)
#         user.set_password(password)
#         user.save()
#         refresh = RefreshToken.for_user(user)
#
#         return Response(
#             {
#                 "status": "success",
#                 'user_id': user.id,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token)
#             })
