from rest_framework import serializers
from movie_app.models import Director, Movie, Review

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



