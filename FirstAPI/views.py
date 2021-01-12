from django.shortcuts import render
from .models import Post, Tag
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializiers import (
    PostListSerializer, 
    TagListSerializer, 
    PostDetailSerializer, 
    TagDetailSerializer, 
    PostCreateSerializer, 
    TagCreateSerializer)

# Create your ws here.


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


# @api_view(['GET'])
# def posts_list(request):
#     posts = Post.objects.all()
#     ser = PostListSerializer(posts, many=True)
#     return Response(data={'success':True, 'data' :ser.data})



class TagListView(ListAPIView):
    serializer_class = TagListSerializer
    queryset = Tag.objects.all()


# @api_view(['GET'])
# def tag_list(request):
#     tags = Tag.objects.all()
#     ser = TagListSerializer(tags, many=True)
#     return Response(data={'success': True, 'data': ser.data})


class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = "pk"
    lookup_url_kwarg = "post_id"


# @api_view(['GET'])
# def post_detail(request, post_id):
#     post = Post.objects.get(id = post_id)
#     ser = PostDetailSerializer(post)
#     return Response(data={'success': True, 'data': ser.data})


class TagDetailView(RetrieveAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()
    lookup_field = "pk"
    lookup_url_kwarg = "tag_id"


# @api_view(['GET'])
# def tag_detail(request, tag_id):
#     tags = Tag.objects.get(id = tag_id)
#     ser = TagDetailSerializer(tags)
#     return Response(data={'success': True, 'data': ser.data})


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer

# @api_view(['POST'])
# def post_create(request):
#     ser = PostCreateSerializer(data=request.data)
#     ser.is_valid(raise_exception=True)
#     post = Post.objects.create(**ser.data)
#     return Response(data={'success': True, 'data': ser.data})


class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer


# @api_view(['POST'])
# def tag_create(request):
#     ser = TagCreateSerializer(data=request.data)
#     ser.is_valid(raise_exception=True)
#     tag = Tag.objects.create(**ser.data)
#     return Response(data={'success': True, 'data': ser.data})