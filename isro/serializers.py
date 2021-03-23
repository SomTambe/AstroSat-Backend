from rest_framework import serializers
from .models import source
from pub.serializers import *
from pub.models import *

"""
class SourceSerializer(serializers.ModelSerializer)

Arguments:
    Input:
        Django object of the `source` model, not a QuerySet.

    Output:
        Python dictionary of with the fields as instructed.
"""
class SourceSerializer(serializers.ModelSerializer):
    pubs = PubSerializer(many=True, read_only=True)

    class Meta:
        model = source
        exclude = ('id')
        depth=1

"""
class GetSource(serializers.ModelSerializer)

Arguments:
    Input:
        Django object of the `source` model, not a QuerySet.

    Output:
        Python dictionary of with the fields as instructed.
"""
class GetSource(serializers.ModelSerializer):
    class Meta:
        model = source
        fields = ('ra','dec','name','astrosat')

