from rest_framework import serializers
from .models import FoodCategory, FoodItem

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['id', 'name']

class FoodItemSerializer(serializers.ModelSerializer):
    category = FoodCategorySerializer(read_only=True)  # GET işlemi için
    category_id = serializers.PrimaryKeyRelatedField(  # POST/PUT için
        queryset=FoodCategory.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = FoodItem
        fields = [
            'id',
            'name',
            'description',
            'price',
            'is_available',
            'created_at',
            'updated_at',
            'image_food',
            'category',
            'category_id'
        ]
