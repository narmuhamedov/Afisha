from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorsSerializers, MoviesSerializers, ReviewSerializer
from movie_app.models import Director, Movie, Review
from rest_framework import status

#list_view GET POST
@api_view(['GET', 'POST'])
def directors_list_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorsSerializers(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print(request.data)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorsSerializers(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MoviesSerializers(movies, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        print(request.data)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director)
        return Response(data=MoviesSerializers(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def reviews_list_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        print(request.data)
        text = request.data.get('text')
        movie_id = request.data.get('movie')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id,
                                        stars=stars)

        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)


#detail_view GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Direct not found'})
    if request.method == 'GET':
        data = DirectorsSerializers(director).data
        return Response(data=data)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorsSerializers(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'movie not found'})
    if request.method == 'GET':
        data = MoviesSerializers(movies).data
        return Response(data=data)

    elif request == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    elif request.method == 'PUT':

        movies.title = request.data.get('title')

        movies.description = request.data.get('description')

        movies.duration = request.data.get('duration')

        movies.director_id = request.data.get('director')

        movies.save()

        return Response(data=MoviesSerializers(movies).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'reviews not found'})
    if request.method == 'GET':
        data = ReviewSerializer(review, many=False).data
        return Response(data=data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)