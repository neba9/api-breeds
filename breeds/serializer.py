from rest_framework import serializers
from .models import Breeds

class BreedSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'purchaser', 'name', 'description', 'height', 'weight' )
    model = Breeds



