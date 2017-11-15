# Project Movie Trailer Website
# Demetra Skl, Aug '17
# Reference: https://classroom.udacity.com/courses/ud036

import media
import fresh_tomatoes

# Instances of class Movie
avatar = media.Movie(
    "Avatar",
    "A story about humans trying to invade an alien world",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

seriesUnfortunateEvents = media.Movie(
    "A Series of Unfortunate Events",
    "Three siblings try to find a new home",
    "https://upload.wikimedia.org/wikipedia/en/c/cb/A_Series_Of_Unfortunate_Events_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=fccho1IyX8Y")

harryPotter = media.Movie(
    "Harry Potter and the Chamber of Secrets",
    "Harry Potter returns to Hogwarts for a second time",
    "https://i.pinimg.com/originals/f1/6a/d3/f16ad3ec88c9b60cf7e1681c521a8b01.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1bq0qff4iF8")

madagascar = media.Movie(
    "Madagascar",
    "A lion raised in a NY zoo returns to Africa",
    "https://upload.wikimedia.org/wikipedia/en/3/36/Madagascar_Theatrical_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=dm-eiFVtRws")

narnia = media.Movie(
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe",
    "Three siblings enter a magical world and fight against the White Witch",
    "https://upload.wikimedia.org/wikipedia/en/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg",  # NOQA
    "https://www.youtube.com/watch?v=LshOd31d-yE")

pirates = media.Movie(
    "Pirates of the Caribbean: The Curse of the Black Pearl",
    "A story of pirates",
    "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",  # NOQA
    "https://www.youtube.com/watch?v=naQr0uTrH_s")

# List of movie objects
movies = [
    avatar,
    seriesUnfortunateEvents,
    harryPotter,
    madagascar,
    narnia,
    pirates]
# Generate HTML file of website
fresh_tomatoes.open_movies_page(movies)
