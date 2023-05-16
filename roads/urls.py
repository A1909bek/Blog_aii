from django.urls import path
from users.views import CustomUserViewSet
from posts.views import PostViewSet,CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',CustomUserViewSet)
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)

urlpatterns = router.urls
