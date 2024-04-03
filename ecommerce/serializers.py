from rest_framework import serializers
from .models import ECommerceApplication


class ECommerceApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECommerceApplication
        exclude = ['platform', 'store_url']

class ECommerceApplicationStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECommerceApplication
        fields = ['email','platform', 'store_url']