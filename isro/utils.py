from .models import *
import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions, status
from pub.models import *
from .serializers import *

"""
function make_card(request)

Arguments:
    Input:
        request : Django request object.

    Output:
        src : a source object, which will then be serialized by the view I have created in views.py. If unsuccessful, it returns a 404_NOT_FOUND request.
"""
def make_card(request):
    # assuming request is a POST request.
    # fields = {'ra','dec'}
    body = request.POST.dict()
    for b in body:
        body=json.loads(b)
    print("body=",body)
    src = get_object_or_404(source, ra=body['ra'], dec=body['dec'])
    return src

"""
function add_src(request)

Arguments:
    Input:
        request : Django request object.

    Output:
        src : Response object, 201 if the object is successfully created, or else, 404 or 406.
"""
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

"""
function add_pub(request)

Arguments:
    Input:
        request : Django request object.

    Output:
        src : Response object, 201 if the object is successfully created, or else 404.
"""
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

"""
function send_data(request)

Arguments:
    Input:
        request : Django request object.

    Output:
        src : Response object with the data of all sources of all the available fields in JSON format.
"""
def send_data(request):
    # assuming request is a GET request.
    # returning parameters for a source = [{'name','ra','dec','astrosat'}, ...]
    ser = [SourceSerializer(s).data for s in source.objects.all()]
    return Response(ser, status=status.HTTP_200_OK)

