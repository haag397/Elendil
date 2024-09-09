"""_summary_
    """

from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from core.models import UserData
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# from .serializers.serializers import UserDataSerializer
from core.serializers import UserDataSerializer


# class User(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

#     queryset = UserData.objects.all()
#     serializer_class = UserDataSerializer

#     def get(self, request, *args, **kwargs):
#         data = request.data
#         print(data)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         print(data)
#         return self.create(request, *args, **kwargs)
class User(APIView):
    permission_classes = [IsAuthenticated]

    def get(self):
        return Response({"message": "Hello, world!"})
