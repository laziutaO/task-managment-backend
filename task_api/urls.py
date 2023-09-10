from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task_api import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('topic', views.UserProfileTopicVeiwSet)

task_router = DefaultRouter()
task_router.register('task', views.UserProfileTaskVeiwSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
    path('topic/', include(task_router.urls))
]