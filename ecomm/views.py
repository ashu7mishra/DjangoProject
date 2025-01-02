from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from tutorial.quickstart.serializers import UserSerializer

from .models import ShippingAddress, User
from .serializers import UserSerializer, ShippingAddressSerializer, CreateShippingAddressSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShippingAddressListCreateAPIView(GenericAPIView):

    def post(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        serializer = CreateShippingAddressSerializer(request.body)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        shipping_address = ShippingAddress(
            street=serializer.validated_data['street'],
            city=serializer.validated_data['city'],
            state=serializer.validated_data['state'],
            zipcode=serializer.validated_data['zipcode'],
            country=serializer.validated_data['country'],
            user=user
        )

        shipping_address.save()

        return Response(ShippingAddressSerializer(
            shipping_address
        ).data, status=status.HTTP_201_CREATED)

