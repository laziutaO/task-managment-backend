from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings 
from rest_framework.permissions import IsAuthenticated

from task_api import serializers,models, permissions


# Create your views here.
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileTaskVeiwSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile tasks"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileTaskSerializer
    queryset = models.ProfileTask.objects.all()
    permission_classes = (permissions.UpdateOwnTask, IsAuthenticated)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('task_text',)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

class UserProfileTopicVeiwSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile tasks"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.TopicSerializer
    queryset = models.Topic.objects.all()
    permission_classes = (permissions.UpdateOwnTask, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)