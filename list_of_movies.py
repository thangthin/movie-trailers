from movie import Movie
# Constant web image url for the movies
TOY_STORY_IMAGE_URL = "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg"  # NOQA 538
SCHOOL_OF_ROCK_IMAGE_URL = "http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v8_aa.jpg"  # NOQA 538
HERMANO_IMAGE_URL = "http://www.gstatic.com/tv/thumb/movies/120713/120713_aa.jpg"  # NOQA 538
# Constant list that store the movies for display
LIST_OF_MOVIES = [
    Movie("Toy Story 3",
          "https://www.youtube.com/watch?v=ZZv1vki4ou4",
          TOY_STORY_IMAGE_URL),
    Movie("School of Rock",
          "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
          SCHOOL_OF_ROCK_IMAGE_URL),
    Movie("Hermano",
          "https://www.youtube.com/watch?v=5vrrRJDN64U",
          HERMANO_IMAGE_URL)
]