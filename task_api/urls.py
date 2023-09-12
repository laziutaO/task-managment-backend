from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task_api import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

topic_router = DefaultRouter()
topic_router.register('profile/<int:id>/topic', views.UserProfileTopicVeiwSet)

task_router = DefaultRouter()
task_router.register('task', views.UserProfileTaskVeiwSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
    path('', include(topic_router.urls)),
    #path('profile/<int:id>/topic/<int:id>/', include(task_router.urls))
]