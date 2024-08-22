from django.core.management.base import BaseCommand
from movie.models import Movie
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.json into the Movie model'

    def handle(self, *args, **kwargs):
        # Construct the full path to the JSON file
        json_file_path = '/Users/alejandrocarmona/Downloads/moviereviewsproject/movie/management/commands/movies.json'

        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            movies = json.load(file)

        # Add products to the database
        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title=movie['title']).first()  # Verifica si la película ya existe en la base de datos
            if not exist:
                # Crear la película en la base de datos
                Movie.objects.create(
                    title = movie['title'],
                    image = 'movie/images/default.jpg',
                    genre = movie['genre'],
                    year = movie['year'],
                    description = movie.get('plot') 
                )

        #self.stdout.write(self.style.SUCCESS(f'Successfully added {cont} products to the database'))