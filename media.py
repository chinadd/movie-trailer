##########################################
# Project 3: Movie Website
# Date Started: 10/24/2017
# Date Completed: 10/24/2017
# Submitted by: Xing Du
##########################################

######################################## Media File ####################################################
# Description: This file creates the class Movie to allow for instances of this class to be used in the
#              entertainment.py file. This definition of the class Movie was obtained through the course
########################################################################################################
class Movie(object):
    """ Attributes:
    movie_title = title of Movie
    poster_image_url = url of movie poster
    trailer_youtube_url = url of movie trailer"""

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
         self.title = movie_title
         self.poster_image_url = poster_image_url
         self.trailer_youtube_url = trailer_youtube_url
