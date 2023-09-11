from rest_framework import serializers
from task_api  import models

    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
    
class ProfileTaskSerializer(serializers.ModelSerializer):
    """Serializers profile tasks"""

    class Meta:
        model = models.ProfileTask
        fields = ('id', 'user_profile', 'task_text', 'completed_box', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

class TopicSerializer(serializers.ModelSerializer):
    """Serializers profile topics"""

    class Meta:
        model = models.Topic
        fields = ('id', 'user_profile', 'topic_name', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True},
                        'created_on': {'read_only': True}}
    