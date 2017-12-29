from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ksiazka
from .serializers import KsiazkaSerializer
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from .CSVImporter.CSVImporter import CSVImporter
from io import TextIOWrapper

class KsiazkaList(APIView):


    def get(self,request):
        ksiazka = Ksiazka.objects.all()
        serializer = KsiazkaSerializer(ksiazka, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class CsvImport(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (authentication.JWTAuthentication,)

    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
        #file_obj = request.FILES['file']
        # do some stuff with uploaded file
        #with open(filename, 'r') as f:
        #    first_line = f.readline()
        csvImporter = CSVImporter()
        first_line = csvImporter.importFromFile(file_obj)

        data = {'file': first_line}
        response = Response(data,status=204)
        response.data = data
        file_obj.close()
        return Response(data)

