from django.shortcuts import render
import pandas as pd
from app.models import Movie

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def csv_to_model(request):
    all_csv_data = pd.read_csv(r'movies.csv')

    if request.method == "POST":

        for i in range(len(all_csv_data.index)):
            r = all_csv_data.loc[i]
            Title = r.title
            Genres = r.genres
            Character_name_and_cast = r.character_name_and_cast
            Overview = r.overview
            Release_date = r.release_date
            Tagline = r.tagline
            Vote_average = r.vote_average
            Vote_count = r.vote_count

            instance = Movie(title=Title, genres=Genres, character_name_and_cast=Character_name_and_cast, overview=Overview, release_date=Release_date, tagline=Tagline, vote_average=Vote_average, vote_count=Vote_count)
            instance.save()
        return render(request, 'app/home.html')

    return render(request, 'app/csv.html', {'data': all_csv_data})