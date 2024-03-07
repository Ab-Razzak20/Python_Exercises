## 04-multimedia_store
'''
Exercise 4.1: Put the DVDs in the back
After taking a walk around the store, you see that there were many DVDs lying around 
in the floor. Many customers found it really weird as they thought this was really dirty. 
So as a first step as manager you inform your colleagues to pick up every DVD lying on 
the floor and add them at the back of the stack closest to them.

'''

def add_dvd_to_stack(dvd_stack , lying_dvd):
    '''(list , str) --> updated_list
    Adds lying_dvd at the end of the dvd_stack.
    '''

    dvd_stack.append(lying_dvd)

    return dvd_stack

'''
Exercise 4.2: Removing duplicates from display
With all the lying DVDs cleared up, you now turn your attention to the front porch of 
the shop and check the DVDs on display. You notice that there were many repeated DVDs 
of the same movie lying around. You realize that might be one of the reasons for the 
lower number of customers turning in lately. So you set forth to remove the duplicates 
from the front display to clear up spots for different DVDs.'''

def remove_duplicates(display_stack):
    '''(list) --> list
    Removes duplicate dvd from the stack, display_stack.
    '''
    updated_display_stack = list(set(display_stack))

    return updated_display_stack

'''Exercise 4.3: Category based movie organization
The store started to look a bit lively with the above steps, with few more customers 
coming in. But, you see that many are leaving empty handed and frustrated. So, you 
look around and see if everything is proper. As you were checking, you realised that
the movies were not at all sorted according to their genres/categories.

As such you come back to your desk and look up in your computer if you could somehow 
find all the movies and their categories that are there in the shop. Lucky enough you 
found a file containing all the movie names and their category well organised as a 
Python dictionary. So you seat on your desk and start coding to organise the movies 
based on their categories. You decide that after this organisation you will ask your 
colleagues to take one category section each and organise the movies according. With 
that in mind, build the function category_sort(movie_name) which does the following 
tasks.

Tasks
- Given the dictionary, movie_name, which contains each movie names as a key and its 
category as the value, create another dictionary which has the categories as its keys 
and the movies with the same categories as the values (stored in a list).
'''
def category_sort(movie_name):
    '''dict -> dict
    returns dictionary which has the categories as its keys and the movies 
    with the same categories as the values (stored in a list)'''

    category_based_movies = {}
    # for genre in movie_name.values():
    #     category_based_movies[genre] = []
    # for movie, genre in movie_name.item():
    #     category_based_movies[genre].append(movie)

    for movie, genre in movie_name.items():
        if genre not in category_based_movies:
            category_based_movies[genre] = [movie]
        else:
            category_based_movies[genre].append(movie)

    return category_based_movies

'''
Exercise 4.4: Do you have this movie?
During lunch time, while you were having coffee with your colleagues they told you that 
they didn't have a system that could search if they have a particular movie at their 
store or not. Many of them agreed that most of the loyal customers have recently reduced 
coming because strolling the entire store for a movie and not finding it really made them
feel helpless in the store.

To solve this you start coding a system that would be accessible to the customers. They 
could query for a movie name and the system will show if the store has that movie or not.

Build a function find_a_movie(category_based_movies , movie) which does the following task.

Tasks
- Grab all the values contained in the dictionary category_based_movies.
- Check if the movie is in the values you collected. If yes return boolean value True, 
  else return False
'''

def find_a_movie(category_based_movies, movie):
    '''
    (dict, str) -> bool 
    Check if the movie is in the dictionary
    '''
    # for genre in category_based_movies.keys():
    #     for cinema in category_based_movies[genre]:
    # for films in category_based_movies.values():
    #     for cinema in films:
    #         if cinema == movie:
    #             return True
    # return False
    movies = [cinema for cinema_lists in category_based_movies.values() for cinema in cinema_lists]
    return movie in movies
    
'''
Exercise 4.5: Can you suggest a horror movie?
After coding up the movie finder, you realise that there might be many customers who 
just want to watch a specific category/genre of movie and not a specific movie itself.
So, you think of giving the customers the list of all the movies you have given a genre 
so that it becomes easier for them to pick.

Build a function  which does the following task.

Tasks
- Returns all the movies there are in a given category from the dictionary.

Disclaimer: The code must throw an assertion error if the category is not right.
'''

def all_movies_in_category(category_based_movies, category):
    '''
    (dict, str) -> list
    Returns all the movies there are in a given category from the dictionary.
    '''
    assert category in category_based_movies.keys(), 'The category is not available'

    return category_based_movies[category]

def generate_squared_dict(n):
    '''
    dict -> dict
    generate and print a dictionary 
    that contains a number (between 1 and n) in the form (x, x*x).
    '''
    dictionary = {}
    for key in range(1, n+1):
        dictionary[key] = (lambda key:key*key)(key)

    return dictionary


if __name__ == '__main__':
    movie_dict = {'Mystery': ['Deep Water'], 
                  'Fantasy': ['Harry Potter and the Chamber of the secrets', 'Lord of the Rings: The Fellowship of the Ring'], 
                  'Action': ['Fast and Furious', 'James Bond : Skyfall']}
    some_movie = {'Action': ['Inception', 'The Dark Knight'], 
                  'Sci-Fi': ['The Matrix', 'Interstellar'], 
                  'Drama': ['Fight Club', 'The Shawshank Redemption', 'Forrest Gump'], 
                  'Biography': ['The Social Network']}
    
    # print(find_a_movie(some_movie, 'Interstellar'))
    # print(find_a_movie(movie_dict, 'Skyfall'))
    # print(all_movies_in_category(movie_dict, 'Fantasy'))
    # print(all_movies_in_category(some_movie, 'Action'))

    print(generate_squared_dict(7))
    