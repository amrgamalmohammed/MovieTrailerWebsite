class Movie(object):
    """
     class containing properties of movie object that need to be encapsulated
     such as movie titles, box art, poster images, and movie trailer URLs.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """ Initiates movie class with data"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
