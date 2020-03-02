from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from comment.models import Comment

class CommentCreateSerializer(ModelSerializer):
  class Meta:
    model = Comment
    exclude = ['created',]

  def validate(self, attrs):
    if(attrs["parent"]):
      if attrs["parent"].post != attrs["post"]:
        raise serializers.ValidationError("something went wrong")

    return attrs  
