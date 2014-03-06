from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Category

class FullNameField(serializers.RelatedField):
    def to_native(self, value):
        user = User.objects.get(username=value)
        return user.get_full_name()


class PostSerializer(serializers.ModelSerializer):
    author = FullNameField()
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    category = serializers.RelatedField()

    class Meta:
        model = Post
        read_only_fields = ('created_on',)


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    post_set = PostSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'url', 'post_set')
