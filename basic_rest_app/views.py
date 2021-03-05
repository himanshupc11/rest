from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# For Rest API
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Class based REST Views
from rest_framework.views import APIView


# Testing
from django.views.decorators.csrf import csrf_exempt


# Generic View
from rest_framework import generics
from rest_framework import mixins

# Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class classBasedIndex(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class ArticleDetailAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'pk'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    


"""
class classBasedIndex(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serialized_articles = ArticleSerializer(articles, many=True)
        return Response(serialized_articles.data)

    def post(self, request):
        serialized_data = ArticleSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
"""
"""
# Create your views here
@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serialized_articles = ArticleSerializer(articles, many=True)
        return Response(serialized_articles.data)

    if request.method == "POST":
        serialized_data = ArticleSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def article_detail(request, pk):
    if request.method == "GET":
        try: 
            article = Article.objects.filter(id=pk)
            print(article)
            article = article[0]
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized_article = ArticleSerializer(article)
        return Response(serialized_article.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        try: 
            article = Article.objects.filter(id=pk)
            print(article)
            article = article[0]
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # data = JSONParser().parse(request)
        serialized_article = ArticleSerializer(article, data=request.data)

        if serialized_article.is_valid():
            serialized_article.save()
            return Response(serialized_article.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try: 
            article = Article.objects.filter(id=pk)[0]
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""




