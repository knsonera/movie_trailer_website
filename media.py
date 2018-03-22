# Movie class provides the way to store movie related information.
# To create an instance (a movie), call the class with three parameters:
# - movie title
# - poster image url
# - youtube video url
# Example:
# the_movie = Movie("The Movie", "http://img.url.com", "youtube-video.url.com")


class Movie:

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
