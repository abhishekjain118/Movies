import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "Story of planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

titanic = media.Movie("Titanic",
                      "Story of a shinking ship",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

print(toy_story.title)
print(toy_story.story_line)
print(toy_story.poster_image_url)
print(toy_story.trailer_youtube_url)

print(avatar.title)
print(avatar.story_line)
print(avatar.poster_image_url)
print(avatar.trailer_youtube_url)

print(titanic.title)
print(titanic.story_line)
print(titanic.poster_image_url)
print(titanic.trailer_youtube_url)


# these print commands are for debugging purpose.
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__) ## it will print documentation of the class
print(media.Movie.__module__)
print(media.Movie.__name__)

movies = [avatar,toy_story,titanic] # List of movie objects
fresh_tomatoes.open_movies_page(movies) # this will generate the HTML page.



