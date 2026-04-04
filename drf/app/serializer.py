from rest_framework import serializers

class InfoSerializer(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.EmailField()
    country=serializers.CharField()
    address=serializers.CharField()
    phone=serializers.CharField()
    gender=serializers.CharField()