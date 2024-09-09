from rest_framework import serializers
from reviews.models import Review
from users.api.serializers import UserInsertSerializer
from books.api.serializers import BookInsertSerializer

class ReviewOnReadSerializer(serializers.ModelSerializer):
    user =UserInsertSerializer()
    book = BookInsertSerializer()
    class Meta:
        model = Review
        exclude = []


class ReviewOnWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['user']