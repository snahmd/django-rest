from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = [
      'user',
      'title',
      'content',
      'image',
      'slug',
      'created',
      'modified_by',
    ]

  #title = serializers.CharField(max_length=200)
  #content = serializers.CharField(max_length=200)

class PostUpdateCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = [
      'title',
      'content',
      'image',
    ]  