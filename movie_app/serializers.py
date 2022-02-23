from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class DirectorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count_movies'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id movie text stars'.split()



class MoviesSerializers(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director_id reviews count_reviews'.split()
        # fields ='__all__'

    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(movie=movie), many=True)
        return serializer.data

class DirectorValidateSerializers(serializers.Serializer):
    name = serializers.CharField(min_length=10, max_length=50)

class MovieCreateValidateSerializers(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=10)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField()


    def validate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count()==0:
            raise ValidationError(f"Director with id = {director_id} not found")
        return director_id

class ReviewCreateValidateSerializers(serializers.Serializer):
    text = serializers.CharField(max_length=50)
    movie = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie_id(self, movie_id):
        if Movie.objects.filter(id=movie_id).count()==0:
            raise ValidationError(f"Movie with id = {movie_id} not found")
        return movie_id


