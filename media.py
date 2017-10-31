import webbrowser


class Movie():
    """ hello all.. this is a class Movie """
    VALID_RATINGS = ['PG','R','PG-13','G']
    def __init__(self,movie_title,movie_story_line,poster_image,trailer_youtube):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
