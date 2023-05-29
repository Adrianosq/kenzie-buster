from rest_framework import serializers
from .models import RatingMovies
from .models import Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=RatingMovies.choices, default=RatingMovies.G)
    synopsis = serializers.CharField(default=None)

    added_by = serializers.CharField(source='user.email', read_only=True)

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_buyed_by(self, obj: MovieOrder):
        return obj.user.email

    def get_title(self, obj: MovieOrder):
        return obj.movie.title
    
    def create(self, validated_data) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
