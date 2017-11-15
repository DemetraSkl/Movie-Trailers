# Project Movie Trailer Website
# Demetra Skl, Aug '17
# Reference: https://classroom.udacity.com/courses/ud036

import webbrowser


class Movie():
    """ This class provides a way to store movie info"""
    # Constructor
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Access trailer weblink
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # Access box art weblink
    def show_poster(self):
        webbrowser.open(self.poster_image_url)
