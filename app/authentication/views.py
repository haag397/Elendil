"""_summary_
    """

from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from core.models import UserData

# from .serializers.serializers import UserDataSerializer
from core.serializers import UserDataSerializer


class User(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def get(self, request, *args, **kwargs):
        data = request.data
        print(data)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        return self.create(request, *args, **kwargs)
