from rest_framework.serializers import ModelSerializer
from ecomm.models import *


class CreateShippingAddressSerializer(ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ["street", "city", "state", "zipcode", "country"]

class ShippingAddressSerializer(ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = "__all__"


class UserSerializer(ModelSerializer):

    shipping_addresses = ShippingAddressSerializer(many=True, read_only=True)
    default_shipping_addresses = ShippingAddressSerializer(read_only=True, allow_null=True)

    class Meta:
        model = User
        fields = "__all__"

