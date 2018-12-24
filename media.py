class Movie:

    def __init__(self, title, description, poster_img_url, trailer_url,
                 imdb_page_url):
        """Holds the information of a movie

        Args:
            title (str): The movie's title.
            description (str): A short synopsis for the movie.
            poster_img_url (str): A url for the movie's poster image.
            trailer_url (str): The Youtube url for the movie's trailer.
            imdb_page_url (str): The url for the movie's IMDB page.
        """
        self.title = title
        self.description = description
        self.poster_img_url = poster_img_url
        self.trailer_url = trailer_url
        self.imdb_page_url = imdb_page_url
