from rest_framework import serializers
from .models import Cat, Target, Mission
import requests

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
        
        #to do
        def validate(self, data):
            response = requests.get('https://api.thecatapi.com/v1/breeds/')
            breeds=[breed['name'].lower() for breed in response.json()]
            if data.lower() not in breeds:
                raise serializers.ValidationError("Incorrect breed")
            return data



class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'
