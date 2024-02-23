#create a list with the average rating for all of these things
#only use map, filter, all, any, len, sum, min, max



movies = [

    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},

    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},

    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},

    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},

    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},

]
# Task 1
# print(list(map(lambda name: name["title"], movies)))


# # Task 1.1 - Find average for all - map, filter, all, ...

# # Dont use for loop or List comp
# print(list(map(lambda x: sum(x["ratings"])/len(x["ratings"]), movies)))

#OR
# def find_avg(movie):
#   sum(movie["ratings"])/len(movie["ratings"])

# movie_avg=map(find_avg, movies)

#Task 1.2 find average for all- map filter, all,...

def find_avg(movie):
  return sum(movie["ratings"])/len(movie["ratings"])
  

movie_with_average_ratings= map(lambda movie:{**movie,"average_rating":find_avg(movie)},movies)
# print(list(movie_with_average_ratings))

#task 2 
#top rated movie
#print the top rated movie name


best_movie = max(

    movies, key=lambda movie: sum(movie["ratings"]) / len(movie["ratings"]))

print(f'The top rated movie is "{best_movie["title"]}"')

##or 
# top_rated_movie= max(movies_average_ratings, key=lambda movie: movie["average_rating"])

##Task 3 
#Movies with ratings more than 4.6
movies_higher= filter(lambda movie: sum(movie["ratings"])/len(movie["ratings"])>4.6, movies)
print(f"The movies higher than 4.6 are {list(map(lambda movie: movie['title'], movies_higher))}")

#first do filter than map

#Task 4
#want the movie names alone in the order of ther rating
sorted_list=sorted(
  movies, key=lambda movie: sum(movie["ratings"])/len(movie["ratings"]), reverse=True
)
print(f"{list(map(lambda movie: movie['title'], sorted_list))}") #did the same thing you did for filter. using the sorted list as a list now.

#to know when to use filter
# It always returns copy of the array (same like map)
# sourceArray.length >= outputArray.length -> True
# input data type === output data type


