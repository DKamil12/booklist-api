from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from users.models import Profile
from books.api.serializers import BookOnReadSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_img', 'bio']
        

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'profile']

    def update(self, instance, validated_data):
        print("from update method")
        
        # update profile info
        profile_data = validated_data.pop('profile', None)
        if profile_data:
            profile = instance.profile
            profile.profile_img = profile_data.get('profile_img', profile.profile_img)
            profile.bio = profile_data.get('bio', profile.bio)
            profile.save()

        # update user info
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        return instance
    

# Serializer to use when a user is a FK
class UserInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return attrs
    
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    