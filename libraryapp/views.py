import os
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from libraryapp.DAO.CategoryDAO import CategoryDAO
from .models import Book
from .serializers import BookSerializer, CategorySerializer, CategoryTreeSerializer
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from .CSVImporter.CSVImporter import CSVImporter
from io import TextIOWrapper
from .DAO.BookDAO import BookDAO
import logging

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

class KsiazkaList(APIView):

    #def get(self, request):
    #    ksiazka = Ksiazka.objects.all().order_by('-syg_ms')[:100:1]
    #    serializer = KsiazkaSerializer(ksiazka, many=True)
    #    return Response(serializer.data)

    def post(self, request):
        ksiazka_DAO = BookDAO()
        ksiazka = ksiazka_DAO.get_book(request.data['query'])
        serializer = BookSerializer(ksiazka, many=True)
        return Response(serializer.data)

    #def put(self, request):
    #    ksiazka_DAO = KsiazkaDAO()
    #    status_response = ksiazka_DAO.addKsiazka(request.data['ksiazka'])
    #    response = Response(status_response.getStatus())
    #    response.status_code=200
    #    return response

    #def delete(self, request):
    #    ksiazka_DAO = KsiazkaDAO()
    #    ksiazka_DAO.deleteKsiazka(request.data['ksiazkaId'])
    #    return Response(status=204)

    #def patch(self, request):
    #    ksiazka_DAO = KsiazkaDAO()
    #    ksiazka_DAO.updateKsiazka(request.data['updateKsiazka'])
    #    return Response(status=204)

class KategoriaList(APIView):

     def get(self, request):
        categories = CategoryDAO().get_category()
        serializer = CategoryTreeSerializer(categories, many=True)
        return Response(serializer.data)

class DictionaryView(APIView):

    def get(self, request):
        dictionary = {}
        types = []
        availability_types =[]

        for type in Book.TYPE_CHOICES:
            types.append(type[0])

        for availability in Book.AVAILABILITY_CHOICES:
            availability_types.append(availability[0])

        dictionary['types'] = types
        dictionary['availability_types'] = availability_types
        return Response(dictionary)


class CsvImport(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (authentication.JWTAuthentication,)

    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
        csv_importer = CSVImporter()
        import_status = csv_importer.importFromFile(file_obj).get_import_status()

        data = {'Import status': import_status}
        response = Response(data,status=204)
        response.data = data
        file_obj.close()
        return Response(data)

# def library_site(request):
#     return render(request, 'librarysite/index.html', {})
class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )