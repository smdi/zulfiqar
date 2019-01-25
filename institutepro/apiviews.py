
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.auth import authenticate


from .models import FeedbackData
from .serializers import FeedbackSerializer , UserSerializer



class FeedbackList(generics.ListCreateAPIView):
    queryset = FeedbackData.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackDeatail(generics.RetrieveDestroyAPIView):
    queryset = FeedbackData.objects.all()
    serializer_class = FeedbackSerializer

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username = username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)










