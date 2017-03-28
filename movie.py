class Movie:
    """A Movie Class for Movie Template"""
    def __init__(self, title, trailer_url, image_path):
        """Initialize movie instance
        Args:
            title (str): title of Movie
            trailer_url (str): url link for movie's trailer_url
            image_path (str): url link for movie's cover image
        """
        self.title = title
        self.trailer_youtube_url = trailer_url
        self.poster_image_url = image_path
