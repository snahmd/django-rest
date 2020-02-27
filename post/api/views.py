from rest_framework.generics import (ListAPIView, 
                                     RetrieveAPIView, 
                                     DestroyAPIView, 
                                     RetrieveUpdateAPIView, 
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


class PostUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostUpdateCreateSerializer
  lookup_field = 'slug'

  def perform_update(self,serializer):
    serializer.save(user = self.request.user)

class PostCreateAPIView(CreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostUpdateCreateSerializer
  
  def perform_create(self,serializer):
    serializer.save(user = self.request.user)