from rest_framework import serializers
from shop.models import Review

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('id', )