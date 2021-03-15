from rest_framework import serializers
from .models import source
from pub.serializers import *
from pub.models import *

class SourceSerializer(serializers.ModelSerializer):
    pubs = PubSerializer(many=True, read_only=True)

    class Meta:
        model = source
        fields = '__all__'
        depth=1
