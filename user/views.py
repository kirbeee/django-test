from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.db import transaction
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from user.serializers import UserSerializer
from user.models import User

class UsersView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # 確保這行正確無誤

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            serializer = UserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
