from rest_framework import serializers
from .models import Cart, Wishlist

class WishListSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'