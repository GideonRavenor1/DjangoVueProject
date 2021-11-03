from django.db.models import Sum, F
from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField("get_total")

    @staticmethod
    def get_total(obj):
        items = OrderItem.objects.filter(order_id=obj.pk).only('price', 'quantity').aggregate(total=Sum(F('price') * F('quantity')))
        return items['total']

    class Meta:
        model = Order
        fields = "__all__"


