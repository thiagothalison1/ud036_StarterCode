from fresh_tomatoes import open_movies_page
from json import load
from movies_list import MoviesList

if __name__ == "__main__":
    movies = MoviesList()

    # Opens the json file containing the movies data
    with open('./data/movies.json') as movies_data:
        movies_data_obj = load(movies_data)
        # It registers each movie on the movies list
        for movie_key, movie_info in movies_data_obj.iteritems():
            movies.register_movie(movie_info["title"],
                                  movie_info["description"],
                                  movie_info["poster_img_url"],
                                  movie_info["trailer_url"],
                                  movie_info["imdb_page_url"])

    # It creates and opens a browser with the movies
    open_movies_page(movies.list)
