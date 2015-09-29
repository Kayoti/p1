#import modules
import webbrowser
class movie():
    """A class to process movie related data

    This class creates instances of data related to a specific movie
    In this class information such as title storyline image trailer url
    are instantiated for text display and video playback purposes

    Attributes:
        movie_title: A String  to display movie title.
        movie_storyline: A String  to display movie storyline.
        poster_image_url: A String  contains url for an image.
        trailer_youtube: A String contains url for a video for playback
    """
    def __init__(self,movie_title, movie_storyline,poster_image_url,trailer_youtube):
        """Inits movie Class with
            movie_title,movie_storyline,poster_image_url,trailer_url
        """
        self.title= movie_title
        self.storyline= movie_storyline
        self.poster_image=poster_image_url
        self.trailer=trailer_url
    def play_trailer(self):
        """Performs video playback of the trailer url link supplied using
            webbrowser module
        ."""
        webbrowser.open(self.trailer)
        
