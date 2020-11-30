from rest_framework import serializers
from .models import Coronagevallen

class coronaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coronagevallen 
        fields = ('id', 'land' , 'aantalInwoners', 'positievegevallen')