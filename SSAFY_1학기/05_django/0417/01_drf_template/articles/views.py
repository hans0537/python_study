from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # GET 아니면 POST만 취급 할거기에 else 는 안됨
    elif request.method == "POST":
        serializer = ArticleListSerializer(data=request.data)
        # raise_exception=True 를 인자로 보내주면 
        # 유효성 실패하면 400에러 메세지를 알아서 처리해준다
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "GET":
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        # 기존에 있는 article 객체에 받아온 정보를 덮어씌운다.
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])    
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 어떤 article에 대한 댓글인지 인자에 넣어주면 자동으로 저장후 db적용
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def comment_detail(request, comment_pk):
    if request.method == 'GET':
        comment = get_object_or_404(Comment, pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

# @api_view(['POST'])
# def comment_create(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         # 어떤 article에 대한 댓글인지 인자에 넣어주면 자동으로 저장후 db적용
#         serializer.save(article=article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)