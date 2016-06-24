from rest_framework import serializers
from models import Ad, Category


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer to represent the Category model """
    class Meta:
        model = Category
        fields = ("title", )

class AdSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Ad model """
    class Meta:
        model = Ad
        fields = ("user", "category", "title", "description", "phone", "website", "facebook", "email", "location")