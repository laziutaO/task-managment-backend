from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task_api import views

router = DefaultRouter()
router.register('test-viewset', views.TestViewSet, base_name = 'test-viewset')

urlpatterns = [
    path('', include(router.urls))
]