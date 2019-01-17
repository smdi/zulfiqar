
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import FeedbackData
from .serializers import FeedbackSerializer , UserSerializer



class FeedbackList(generics.ListCreateAPIView):
    queryset = FeedbackData.objects.all()
    serializer_class = FeedbackSerializer



class FeedbackDeatail(generics.RetrieveDestroyAPIView):
    queryset = FeedbackData.objects.all()
    serializer_class = FeedbackSerializer

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
















