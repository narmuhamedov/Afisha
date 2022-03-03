from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorsSerializers, MoviesSerializers, ReviewSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from . serializers import UserCreateSerializer


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorsSerializers


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializers


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class DirectorUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorsSerializers
    lookup_field = 'id'



class MovieUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializers
    lookup_field = 'id'


class ReviewsUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

class RegisterAPIView(APIView):
    serializer_class = UserCreateSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(**serializer.validated_data)
        return Response(data={'message': 'User created'},
                        status=status.HTTP_201_CREATED)
