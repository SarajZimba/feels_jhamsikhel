from order.models import Order, OrderDetails
from menu.models import Menu
from rest_framework import serializers
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = [
            "created_at",
            "updated_at",
            "status",
            "is_deleted",
            "sorting_order",
            "is_featured"
        ]
    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    
class OrderDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetails
        exclude = [
            "created_at",
            "updated_at",
            "status",
            "is_deleted",
            "sorting_order",
            "is_featured"
        ]

    def create(self, validated_data):
        return OrderDetails.objects.create(**validated_data)
        
class RatingOrderDetailsSerializer(serializers.ModelSerializer):
    productId = serializers.SerializerMethodField()
    class Meta:
        model = OrderDetails
        exclude = [
            "created_at",
            "updated_at",
            "status",
            "is_deleted",
            "sorting_order",
            "is_featured"
        ]

    def create(self, validated_data):
        return OrderDetails.objects.create(**validated_data)
    
    def get_productId(self, obj):
        menu_id = Menu.objects.get(item_name=obj.itemName).id
        return menu_id
    
class CustomOrderDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetails
        exclude = [
            "created_at",
            "updated_at",
            "status",
            "is_deleted",
            "sorting_order",
            "is_featured"
        ]

from django.utils import timezone
import pytz   
class CustomOrderWithOrderDetailsSerializer(serializers.ModelSerializer):
    products = CustomOrderDetailsSerializer(source='orderdetails_set', many=True, read_only=True)
    updated_time = serializers.SerializerMethodField()
    # bot = serializers.SerializerMethodField()
    # kot = serializers.SerializerMethodField()
    # tableNumber = serializers.SerializerMethodField()
    class Meta:
        model = Order
        exclude = [
            "created_at",
            "updated_at",
            "status",
            "is_deleted",
            "sorting_order",
            "is_featured"
        ]

    # def get_bot(self, obj):
    #     return int(obj.orderdetails_set.first().botID) if (obj.orderdetails_set.first() is not None and obj.orderdetails_set.first().botID is not None)else None
    
    # def get_kot(self, obj):
    #     return int(obj.orderdetails_set.first().kotID) if (obj.orderdetails_set.first() is not None and obj.orderdetails_set.first().kotID is not None) else None
    
    # def get_tableNumber(self, obj):
    #     return str(obj.table_no) if (obj.orderdetails_set.first() is not None and obj.table_no is not None) else None
    def get_updated_time(self, obj):
        local_tz = pytz.timezone('Asia/Kathmandu')
        return obj.orderdetails_set.order_by('id').last().created_at.astimezone(local_tz).strftime("%I:%M %p") if (obj.orderdetails_set.last() is not None) else None
    
