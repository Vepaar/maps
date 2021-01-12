from rest_framework import serializers
from .models import Post, Tag


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title")


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagPostDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class PostDetailSerializer(serializers.ModelSerializer):
    tags = TagPostDetailsSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'

class TagDetailSerializer(serializers.ModelSerializer):
    posts = PostDetailSerializer(many=True)
    class Meta:
        model = Tag
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post
    
    class Meta:
        model = Post
        exclude = ('id', 'tags')


class TagCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        tag = Tag(**validated_data)
        tag.save()
        return tag
    
    class Meta:
        model = Tag
        fields = "__all__"