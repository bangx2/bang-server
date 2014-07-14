from rest_framework import generics
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import permissions


from .models import Bang
from .serializers import BangSerializer


class BangList(generics.ListCreateAPIView):
    queryset = Bang.objects.all()
    serializer_class = BangSerializer


class BangDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bang.objects.all()
    serializer_class = BangSerializer
