import media
import fresh_tomatoes as ft
import tmdbsimple as tmdb

# TMDB API registered key
api_key = "0faa645fefa10d2dc0880b20e8ecd232"

class EntertainmentCenter(object):
    """
    This class creates a list of movies that are generated in an HTML file
    You can generate your own movies by providing a path to text file containing titles that you want
    us to view, or you can just simply view our picks!
    """

    def __init__(self, file_path=None):
        self.file_path = file_path

    def generate_movies_page(self):
        """
        Try to get info of your favourite movies or just display pre loaded movies
        """
        movies = []  # List to hold all the movies
        movies_file = None

        if self.file_path is None:
            movies_file = "/defaults.txt"
        else:
            movies_file = self.file_path

        f = open(movies_file, "r")      # Read movies' titles

        tmdb.API_KEY = api_key
        search = tmdb.Search()

        # Loop over all titles
        for title in f:
            response = search.movie(query=title)['results'][0]      # Record the first response
            movie_id = response['id']
            tmdb_movie = tmdb.Movies(movie_id).info(**{'append_to_response': 'trailers'})

            # Construct needed information about movies
            movie_title = tmdb_movie.get('original_title')
            movie_poster = "https://image.tmdb.org/t/p/original" + tmdb_movie.get('poster_path')
            movie_trailer = "http://www.youtube.com/watch?v=" + tmdb_movie.get('trailers')['youtube'][0]['source']
            print(movie_id, " ", movie_title, " ", movie_poster, " ", movie_trailer)

            # Construct movie object and append it to our list
            movie = self.__construct_movie_object(movie_title, movie_poster, movie_trailer)
            movies.append(movie)

        # Attempt to generate final HTML file
        ft.open_movies_page(movies)

    @staticmethod
    def __construct_movie_object(title, poster, trailer):
        """
        Private function to handle the creation of a movie class object from media file
        """
        movie = media.Movie(title, poster, trailer)
        return movie
