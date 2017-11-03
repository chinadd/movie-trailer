import fresh_tomatoes
import media
from media import Movie

# Creating movies to describe the instances of the Class Movie
movie1 = Movie('The sun also rises',
               'https://upload.wikimedia.org/wikipedia/en/d/d0/The_Sun_Also_Rises.jpg',
               'https://www.youtube.com/watch?v=iNGuH5mV6V4')

movie2 = Movie('Let the bullets fly',
               'https://img1.doubanio.com/view/photo/raw/public/p1512562287.jpg',
               'https://www.youtube.com/watch?v=PFoLfRA5ghw')

movie3 = Movie('Crouching Tiger, Hidden Dragon',
               'https://img3.doubanio.com/view/photo/raw/public/p1507810991.jpg',
               'https://www.youtube.com/watch?v=gLpZ_5bHmo8')

movie4 = Movie('Good Will Hunting',
                'https://img3.doubanio.com/view/photo/raw/public/p480965695.jpg',
                'https://www.youtube.com/watch?v=nH9LZOXBMUE')

# Create a list of movies
movies = [movie1, movie2, movie3, movie4]
# Generate HTML file using the movies list
fresh_tomatoes.open_movies_page(movies)
