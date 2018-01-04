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
from .DAO.KsiazkaDAO import KsiazkaDAO

class KsiazkaList(APIView):

    def get(self, request):
        ksiazka = Ksiazka.objects.all().order_by('-syg_ms')[:100:1]
        serializer = KsiazkaSerializer(ksiazka, many=True)
        return Response(serializer.data)

    def post(self, request):
        ksiazka_DAO = KsiazkaDAO()
        ksiazka = ksiazka_DAO.getKsiazka(request.data['query'])
        serializer = KsiazkaSerializer(ksiazka, many=True)
        return Response(serializer.data)

        return Response(request.data)

    def put(self, request):
        ksiazka_DAO = KsiazkaDAO()
        ksiazka_DAO.addKsiazka(request.data['ksiazka'])
        return Response(status=204)

    def delete(self, request):
        ksiazka_DAO = KsiazkaDAO()
        ksiazka_DAO.deleteKsiazka(request.data['ksiazkaId'])
        return Response(status=204)

    def patch(self, request):
        ksiazka_DAO = KsiazkaDAO()
        ksiazka_DAO.updateKsiazka(request.data['updateKsiazka'])
        return Response(status=204)


class CsvImport(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (authentication.JWTAuthentication,)

    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
        csvImporter = CSVImporter()
        import_status = csvImporter.importFromFile(file_obj).getImportStatus()

        data = {'Import status': import_status}
        response = Response(data,status=204)
        response.data = data
        file_obj.close()
        return Response(data)

