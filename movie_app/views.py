from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorsSerializers, MoviesSerializers, ReviewSerializers
from movie_app.models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def directors_list_view(request):
    director = Director.objects.all()
    data = DirectorsSerializers(director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    data = MoviesSerializers(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializers(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Direct not found'})
    data = DirectorsSerializers(director).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'movie not found'})
    data = MoviesSerializers(movies).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'reviews not found'})
    data = ReviewSerializers(review).data
    return Response(data=data)