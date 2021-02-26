from rest_framework import serializers
from .models import MovieDetail


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    rating = serializers.CharField(max_length=10)
    release_date = serializers.CharField(max_length=32)
    duration = serializers.CharField(max_length=10)
    description = serializers.CharField()

    class Meta:
        model = MovieDetail
        fields = '__all__'
