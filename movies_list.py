from media import Movie


class MoviesList:
    """This class is an abstraction for a list of movies
    """

    def __init__(self):
        self.list = []

    def register_movie(self, title, description, poster_img_url, trailer_url,
                       imdb_page_url):
        """Registers the movie information in a list of movies

        Note:
            The list of movies can be retrieved by using the attribute list

        Args:
            title (str): The movie's title.
            description (str): A short synopsis for the movie.
            poster_img_url (str): A url for the movie's poster image.
            trailer_url (str): The Youtube url for the movie's trailer.
            imdb_page_url (str): The url for the movie's IMDB page.
        """
        movie = Movie(title, description, poster_img_url, trailer_url,
                      imdb_page_url)
        self.list.append(movie)
