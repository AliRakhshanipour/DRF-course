from rest_framework import serializers
from profiles_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """serializers a user profile"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'], name=validated_data['name'], password=validated_data['password'])
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    """seializer profile feed item"""
    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_txt', 'created_on',)
        # extra_kwargs = {
        #     'user_profile': {
        #         'read_only': True
        #     }
        # }
