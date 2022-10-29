class Movie:
    __watched_movies = 0

    def __init__(self, name, director, watched=False):
        self.name = name
        self.director = director
        self.watched = watched

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if not self.watched:
            Movie.__watched_movies +=1
            self.watched = True

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"

# Part below is test code from example

first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)

#################################### TASK CONDITION ############################
'''
                               09.  *Movie
Create a class Movie. The __init__ method should receive a name and a director. 
It should also have a default value of an attribute called watched set to False. 
There should also be a class attribute __watched_movies which will keep track of
the number of all the watched movies. The class should have the following methods:
•	change_name(new_name: str) - changes the name of the movie
•	change_director(new_director: str) - changes the director of the movie
•	watch() - change the watched attribute to True and increase the total 
watched movies class attribute (if the movie is not already watched)
•	__repr__() - returns "Movie name: {name}; Movie director: {director}. 
Total watched movies: {__watched_movies}"

_______________________________________________
Example

Test Code	(no input data in this task)

first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)

Output
Movie name: Inception; Movie director: Me. Total watched movies: 2
Movie name: The Matrix; Movie director: The Wachowskis. Total watched movies: 2
Movie name: My Movie; Movie director: Shane Black. Total watched movies: 2

'''
