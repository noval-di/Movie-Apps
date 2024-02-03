import os
import json
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Imports movies from movies.json to the database'

    def handle(self, *args, **options):
        file_path = '~/Desktop/Test Omni/movie_web/data/movies.json'
        expanded_path = os.path.expanduser(file_path)
        with open(expanded_path) as json_file:
            data = json.load(json_file)

        for movie_data in data:
            Movie.objects.create(
                name=movie_data['name'],
                description=movie_data['description'],
                imgPath=movie_data['imgPath'],
                duration=movie_data['duration'],
                genre=movie_data['genre'],
                language=movie_data['language'],
                mpaaRatingType=movie_data['mpaaRating']['type'],
                mpaaRatingLabel=movie_data['mpaaRating']['label'],
                userRating=movie_data['userRating']
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported movies'))
