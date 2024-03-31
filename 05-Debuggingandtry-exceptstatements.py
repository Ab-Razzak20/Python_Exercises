'''' Exercise 5.2: Semantic error!
The calculate_years_to_double() function is meant to find out how long it takes for a given amount of money(principal) to double with compound interest. Unfortunately, the function contains mistakes that prevents it from working correctly. Please identify and correct the mistake in the function.
Note that the interest rate is provided in the range (0 to 100], representing a percentage.

Tasks
- [ ] Write an assertion statement which stops the program if the principal is negative or the annual_interest_rate is not within the range (0, 100].
- [ ] Fix the given code.

'''

def calculate_years_to_double(principal, annual_interest_rate):
    '''(int , int) -> int
	Calculate the number of years required for the given principal to exceed double 
    with the provided annual interest rate using compound interest.
    '''
    
    assert principal >= 0 and 0 <= annual_interest_rate < 100, 'Principal can not be negative and annual interest rate is within the range (0, 100]'

    target_amount = principal * 2
    amount = principal
    years = 0
	
    while amount < target_amount:
        amount += principal * annual_interest_rate / 100
        years += 1
        
        amount = principal

    return years
'''
Exercise 5.3: Accepting the Exceptions
Get on to the next function, list_ratios(list_1 , list_2). This function is trivial
but is a bit tricky to handle. The function takes in 2 arguments, both of which are lists, 
and returns a new list whose element at index, i, is given by 
new_list[i] = list_1[i] / list_2[i].
'''

def list_ratios(list_1 , list_2):
    '''(list , list) -> list
    Returns a new list which has the elements list_1 / list_2.
    '''

    #TODO: Use an assertion statement which checks if the length of lists are same.
    assert len(list_1) == len(list_2), 'The length of the given lists must be same'
    new_list = []

    for i in range(len(list_1)):

        try:
            new_list.append(list_1[i]/list_2[i])
        except ZeroDivisionError:
            new_list.append('nan')
        except TypeError:
            new_list.append(None)
        
    return new_list


