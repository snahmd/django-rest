from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(
    view_name = 'post:detail',
    lookup_field = 'slug'
    #view_name='namespace:name'
  )
  #username = serializers.SerializerMethodField(method_name='username_new')
  username = serializers.SerializerMethodField()
  class Meta:
    model = Post
    fields = [
      'username',
      'title',
      'content',
      'image',
      'url',
      'created',
      'modified_by',
    ]
  #def username_new(self, obj):  
  #  return str(obj.user.username)

  def get_username(self, obj):  
    return str(obj.user.username)

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

  #def create(self, validated_data):
  #  return Post.objects.create(user = self.context["request"].user, **validated_data)

  #def update(self, instance, validated_data):
  #  instance.title = validated_data.get('title', instance.title)
  #  instance.content = validated_data.get('content', instance.title)
  #  instance.image = validated_data.get('image', instance.title)
  #  instance.save()
  #  return instance

  #def validate_title(self, value):
  #  if value == "oguzhan":
  #    raise serializers.ValidationError("Bu değer olmaz.")
  #  return value  

  #def validate(self, attrs):
  #  if attrs["title"] == "ahmed":
  #   raise serializers.ValidationError("olmaz")
  #  return attrs