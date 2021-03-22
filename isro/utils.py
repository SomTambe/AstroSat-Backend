from .models import *
import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions, status
from pub.models import *
from .serializers import *

def make_card(request):
    # assuming request is a POST request.
    # fields = {'ra','dec'}
    body = request.POST.dict()
    for b in body:
        body=json.loads(b)
    print("body=",body)
    src = get_object_or_404(source, ra=body['ra'], dec=body['dec'])
    return src

def add_src(request):
    # assuming request is a POST request.
    # fields = {'name','ra','dec','astrosat'}
    body = request.POST.dict()
    try:
        name = body['name']
        ra = body['ra']
        dec = body['dec']
        astrosat = body['astrosat']
    except KeyError:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        src = source(name=name, ra=ra, dec=dec, astrosat=astrosat)
        src.save()
        return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

def add_pub(request):
    # assuming request is a POST request.
    # fields = {'title','link','sources'}
    body = request.data
    try:
        title = body['title']
        link = body['link']
        sources = body.getlist('sources') # This should be a list of 'names' of sources.
    except KeyError:
        return Response(status=status.HTTP_404_NOT_FOUND)

    pub = pubs(title=title, link=link)
    pub.save()
    for s in sources:
        src = get_object_or_404(source, name=s)
        pub.add_src(src)
    return Response(status=status.HTTP_201_CREATED)

def send_data(request):
    # assuming request is a GET request.
    # returning parameters for a source = [{'name','ra','dec','astrosat'}, ...]
    ser = [GetSource(s).data for s in source.objects.all()]
    return Response(ser, status=status.HTTP_200_OK)

