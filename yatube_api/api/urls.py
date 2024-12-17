from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupsViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupsViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('<str:version>/', include(router.urls)),
    path('<str:version>/', include('djoser.urls.jwt')),
]
