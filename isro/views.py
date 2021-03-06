from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import *
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .serializers import *

# @csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the ISRO index.")

class CardView(APIView):
    def get(self, request):
        return HttpResponse("Bad Request.", status=400)
    
    def post(self, request):
        s = make_card(request) # got the source we wanted
        s = SourceSerializer(s)
        return Response(s.data, status=status.HTTP_200_OK)

class AddSource(APIView):
    def get(self, request):
        return HttpResponse("Bad Request.", status=400)

    def post(self, request):
        return add_src(request)

class AddPub(APIView):
    def get(self, request):
        return HttpResponse("Bad Request.", status=400)
    
    def post(self, request):
        return add_pub(request)

class GetData(APIView):
    def get(self, request):
        return send_data(request)

    def post(self, request):
        return HttpResponse("Bad Request.", status=400)
