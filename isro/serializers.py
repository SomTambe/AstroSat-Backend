from rest_framework import serializers
from .models import source
from pub.serializers import *
from pub.models import *

class SourceSerializer(serializers.ModelSerializer):
    pubs = PubSerializer(many=True, read_only=True)

    class Meta:
        model = source
        exclude = ('id')
        depth=1

class GetSource(serializers.ModelSerializer):
    class Meta:
        model = source
        fields = ('ra','dec','name','astrosat')

