import fresh_tomatoes
import media


the_dark_knight = media.Movie("The Dark Knight", "The dark knigt defends Gotham city from the joker and his arch of evil",
                        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

inception = media.Movie("Inception", "A story of dreams",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

oceans_eleven = media.Movie("Oceans Eleven", "Daniel Ocean is out for some serious cash",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
                        "https://www.youtube.com/watch?v=m7lrZK21AX4")

the_italian_job = media.Movie("The Italian Job", " A story about a team of thieves who plan to steal gold from a former associate who double-crossed them",
                        "https://upload.wikimedia.org/wikipedia/en/d/db/Italianjob.jpg",
                        "https://www.youtube.com/watch?v=yTzsEmbP_yo")

furious_seven = media.Movie("Furious 7", "Deckard Shaw (Statham), a rogue special forces assassin seeking to avenge his comatose younger brother, puts Dom and crew in danger once again",
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
                        "https://www.youtube.com/watch?v=yISKeT6sDOg")

troy = media.Movie("Troy", " Achilles leads his Myrmidons along with the rest of the Greek army invading the historical city of Troy, defended by Hector's Trojan army",
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Troy2004Poster.jpg",
                        "https://www.youtube.com/watch?v=znTLzRJimeY")
#print(inception.storyline)
#inception.show_trailer()

movies = [the_dark_knight,inception,oceans_eleven,the_italian_job,furious_seven,troy]

fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)

