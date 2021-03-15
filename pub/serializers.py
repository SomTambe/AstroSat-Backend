from rest_framework import serializers
from .models import pubs

class PubSerializer(serializers.ModelSerializer):
    class Meta:
        model = pubs
        exclude = ('sources',)
