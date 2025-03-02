from rest_framework import viewsets
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .consumers import get_movie_from_omdb

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        # Buscar dados do filme na API OMDb
        title = serializer.validated_data['title']
        movie_data = get_movie_from_omdb(title)

        # Popula o modelo Movie com dados da API
        movie = serializer.save(
            year=movie_data.get('Year'),
            director=movie_data.get('Director'),
            plot=movie_data.get('Plot')
        )

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Create your views here.
