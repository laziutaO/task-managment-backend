from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task_api import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
#router.register('profile/<int:profile_id>/topics', views.UserProfileTopicVeiwSet)
#router.register('profile/<int:profile_id>/topic/<int:topic_id>/task', views.UserProfileTaskVeiwSet)

topic_router = DefaultRouter()
router.register('topics', views.UserProfileTopicVeiwSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    #path('task/', views.UserProfileTaskVeiwSet.as_view()),
    path('', include(router.urls)),
    path('profile/<int:profile_id>/', include(topic_router.urls))

]