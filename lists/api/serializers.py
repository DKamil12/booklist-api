from rest_framework import serializers
from lists.models import List, ListItem, ListFollower
from users.api.serializers import UserInsertSerializer
from books.api.serializers import BookInsertSerializer

class ListOnReadSerializer(serializers.ModelSerializer):
    user = UserInsertSerializer()
    class Meta:
        model = List
        exclude = []


class ListOnWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        exclude = ['user']


# Serializer for nested List FK in other models
class ListInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name']


class ListItemOnReadSerializer(serializers.ModelSerializer):
    list = ListInsertSerializer()
    book = BookInsertSerializer()
    class Meta:
        model = ListItem
        exclude = []


class ListItemOnWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        exclude = []


class ListFollowerOnReadSerializer(serializers.ModelSerializer):
    list = ListInsertSerializer()
    user = UserInsertSerializer()
    class Meta:
        model = ListFollower
        exclude = []


class ListFollowerOnWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListFollower
        exclude = ['user']

    def validate(self, attrs):
        return super().validate(attrs)
