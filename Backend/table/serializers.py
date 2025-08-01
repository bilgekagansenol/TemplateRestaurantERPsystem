from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'is_active', 'created_at']
