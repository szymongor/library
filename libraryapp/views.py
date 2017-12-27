from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ksiazka
from .serializers import KsiazkaSerializer
from rest_framework_simplejwt import authentication
from rest_framework import permissions

class KsiazkaList(APIView):


    def get(self,request):
        ksiazka = Ksiazka.objects.all()
        serializer = KsiazkaSerializer(ksiazka, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class KsiazkaListProtected(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    def get(self,request):
        ksiazka = Ksiazka.objects.all()
        serializer = KsiazkaSerializer(ksiazka, many=True)
        return Response(serializer.data)

    def post(self):
        pass
