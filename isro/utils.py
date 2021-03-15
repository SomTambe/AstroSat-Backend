from .models import *
import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

def make_card(request):
    # assuming request is a POST request.
    body = request.POST.dict()
    src = get_object_or_404(source, name=body['name'])
    return src
