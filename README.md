# Movie Trailer website.

This is a source code for Movie Trailer website.

## What's inside:
- Movie data structure - media.py
- Example of data file - entertainment_center.py
- Web page generator - fresh_tomatoes.py
- Example of launcher

## Getting Started

### Preparing data

To generate web page with movie trailers you will need to format data in a certain way.

Main data structure is **Movie class**.

**Parameters:**

- movie title
- poster image url
- youtube video url

**Example:**
```
awesome_movie = Movie("Awesome Movie", "http://poster.url.com", "youtube-video.url.com")
```

## Building the web page

To generate Movie Trailer website:
- add all your movies to the list
- call method open_movies_page(movie_list) from fresh_tomatoes.py
**fresh_tomatoes.html** will be created.

In **launcher.py** we call this method with our movie list from **entertainment_center.py**.

## Try me!
Follow the steps:
```
$ git clone https://github.com/knsonera/movie_trailer_website.git
$ cd movie_trailer_website
$ python launcher.py
```
Voila, Movie Trailer website is now available in **fresh_tomatoes.html** !

## Opening Movie Trailer website

Method **open_movies_page(movie_list)** opens the page automatically, after the page is ready. 
If it doesn't work, open **fresh_tomatoes.html** in any web browser to see the result.
