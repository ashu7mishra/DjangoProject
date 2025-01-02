from rest_framework.serializers import ModelSerializer
from ecomm.models import *


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class CreateShippingAddressSerializer(ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ["street", "city", "state", "zipcode", "country"]

class ShippingAddressSerializer(ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = "__all__"

