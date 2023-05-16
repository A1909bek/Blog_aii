from .models import Post,Comment
from rest_framework.serializers import ModelSerializer
from users.serializers import CustomUserSerializer

class PostSerializer(ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        