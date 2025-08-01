from rest_framework import serializers
from menu.models import FoodItem
from table.models import Table
from .models import Order, OrderItem
from menu.serializers import FoodItemSerializer
from table.serializers import TableSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    food_item = FoodItemSerializer(read_only=True)
    food_item_id = serializers.PrimaryKeyRelatedField(
        queryset=FoodItem.objects.all(),
        source='food_item',
        write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'food_item', 'food_item_id', 'quantity', 'note']


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(),
        source='table',
        write_only=True
    )
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'table_id', 'created_at', 'is_paid', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(order=order, **item)
        return order
