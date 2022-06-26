from importlib.metadata import requires
from pkg_resources import require
from rest_framework import serializers
from movie.models import Movie, Review, LANGUAGE_CHOICES, STYLE_CHOICES


class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'year']
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, allow_blank=False, max_length=5000)
    year = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
            Create and return a new `Snippet` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.title)
        instance.year = validated_data.get('year', instance.code)
        instance.save()
        return instance
