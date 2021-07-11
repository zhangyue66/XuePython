import media
import time
import fresh_tomatoes


toy_story = media.Movie("Toy Story","a Story about a boy and his toy","https://goo.gl/images/snmmNm","https://www.youtube.com/watch?v=0GZ4KjRwOzk")

#print(toy_story.storyline)

avatar = media.Movie("Avatar","a marine on a alien planet","https://goo.gl/images/snmmNm","https://www.youtube.com/watch?v=0GZ4KjRwOzk")

#print(avatar.storyline)
#print("the move you will be watching is "+avatar.trailer_youtube_url)
#avatar.show_trailer()

#time.sleep(5)

matrix = media.Movie("Matrix","a savior in computer world","www.googel.com","youtube.com")

#print(matrix.title)
#matrix.show_trailer()

dragon = media.Movie("Dragon","a animal that can fly","www.googel.com","youtube.com")

hunger_games = media.Movie("Hunger Games","a killing game that people play","www.sina.com.cn","youtube.com/nba")

movies = [toy_story,avatar,matrix,dragon,hunger_games]

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print("the name of this class Movie is " + media.Movie.__name__)
print(media.Movie.__module__)