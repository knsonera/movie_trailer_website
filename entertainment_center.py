import media

# create instances of Movie class
inception = media.Movie("Inception",
                        "http://bit.ly/2G6FOtx",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")
lego_movie = media.Movie("LEGO Movie",
                         "http://bit.ly/2IEwNGg",
                         "https://www.youtube.com/watch?v=0EqtEPrO5Z4")
lalaland = media.Movie("La La Land",
                       "http://bit.ly/2poy4th",
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8")
shape_of_water = media.Movie("The Shape of Water",
                             "http://bit.ly/2FWROKx",
                             "https://www.youtube.com/watch?v=XFYWazblaUA")
logan = media.Movie("Logan", "http://bit.ly/2FQkOro",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")
whiplash = media.Movie("Whiplash", "http://bit.ly/2GbGwpl",
                       "https://www.youtube.com/watch?v=Df1xkYYbYrY")

# create list of movies
movieList = []
# add movies to the list
movieList.append(inception)
movieList.append(lego_movie)
movieList.append(lalaland)
movieList.append(shape_of_water)
movieList.append(logan)
movieList.append(whiplash)
