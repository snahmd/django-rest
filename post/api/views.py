from rest_framework.generics import (ListAPIView, 
                                     RetrieveAPIView, 
                                     DestroyAPIView, 
                                     UpdateAPIView, 
                                     CreateAPIView,)

from post.models import Post
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer

class PostListAPIView(ListAPIView): 
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  

class PostDetailAPIView(RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostUpdateCreateSerializer
  lookup_field = 'slug'

class PostCreateAPIView(CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostUpdateCreateSerializer
    