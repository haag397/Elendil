"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser
from .models import AdminData
from .serializers import AdminDataSerializer, UserDataSerializer
from django.contrib.auth.models import User


class AdminDataCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = AdminData.objects.all()
    serializer_class = AdminDataSerializer

    def post(self, request):
        email = request.data.get("email")
        firstname = request.data.get("firstname")
        lastname = request.data.get("lastname")
        username = request.data.get("username")
        password = request.data.get("password")
        print(firstname, lastname, username, password)
