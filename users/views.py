from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterGenericAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        data = request.data

        if password != confirm_password:
            return Response({"message": "Passwords are not same!"})

        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists!"})

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

