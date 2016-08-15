#defines the class which we will populate with the movie info
class Movie():
	""" This Class Provides a way to store movie info"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating) :
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating = movie_rating