from rest_framework import serializers
from .models import Article

# Serializer Class
"""class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    email = serializers.EmailField()
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)

        instance.save()
        return instance
"""

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'email', 'date']
