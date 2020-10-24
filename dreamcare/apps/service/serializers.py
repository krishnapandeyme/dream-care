from rest_framework import serializers
from dreamcare.apps.service.models import ServiceCategory, ServiceSubCategory


class ServiceSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceSubCategory
        fields = ['id', 'name', 'category']


class ServiceCategorySerializer(serializers.ModelSerializer):
    subcategories = ServiceSubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'subcategories']






