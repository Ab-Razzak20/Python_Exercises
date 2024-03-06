'''Four of my friends decided to split in half and go to my choice of destination 
but decided to visit different specific places at the same exact time so one group
can video call the other one to show them the live view of the place they are in. 
In this way, everyone thought that they can time-travel and visit both the places 
at the same time.
     My friends told me to come up with a solution so that if they can give the 
exact time in one place, the exact time in the other place will be shown.This way 
a plan to travel the  exquisite places at the perfect times simultaneously. 
''' 

def get_time_timezone():
    '''(None) -> (int,int,int,float,float)
    Returns the current time trisected in hours, minutes, seconds. 
    Along with that also returns the timezone1 and timezone2 as given by the user.
    '''
    current_time = input('Enter your local time in the format: HH:MM:SS( with the 24 hour clock):')
    hours, minutes, seconds = map(int, current_time.split(':'))
    ## Typecast hours, minutes and seconds to integer for using it later on ##
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    ## Get the UTC offset for the current place and the target place ##
    current_timezone = float(input('Enter your local timezone in hours(i.e., -4.5 for GMT-4:30):'))
    target_timezone = float(input('Enter your desired timezone in hours(i.e., +9 for UTC+9:00):'))

    return hours, minutes, seconds, current_timezone, target_timezone


def time_difference(current_timezone, target_timezone):
    '''(float, float) --> float
    Return the difference between target timezone and the current timezone.
    '''
    difference = target_timezone - current_timezone
    return difference

def convert_to_seconds(hours , minutes , seconds , difference):
    '''(int,int,int,float) --> (float , float)
    Returns the hours , minutes , seconds , difference all converted into seconds.
    '''
    current_time_in_sec = hours*3600 + minutes*60 + seconds

    ## Timezones are always given in hours. Eg: +1.5 mean one and half hours ahead of ##
    ## greenwich mean time (GMT) ##
    timezone_diff_in_sec = difference*3600 

    return current_time_in_sec, timezone_diff_in_sec

def target_timezone_time_in_sec(current_time_in_sec , timezone_diff_in_sec):
    '''(float,float) --> float
    Returns target time in seconds from current time and timezone difference.
    '''
    target_time_in_sec = current_time_in_sec + timezone_diff_in_sec

    return target_time_in_sec

def reformat_target_time(target_time_in_sec):
    '''(float) --> (int , int, int)
    Return the calculated hour, minutes and seconds from the target time in seconds.
    '''

    target_hour = target_time_in_sec//3600
    
    ## Hour might be over 24, so..  

    # target_hour = target_hour-12 if target_hour>24 else target_hour  
    target_hour = target_hour%24
    remaining_sec = target_time_in_sec%3600
    target_minutes =  remaining_sec//60
 
    target_seconds = remaining_sec%60

    return target_hour, target_minutes, target_seconds

''' https://www.geeksforgeeks.org/python-string-format-method/ '''

def actual_target_time(target_hour, target_minutes, target_seconds):
    '''(int,int,int) --> (str)
    Returns HH:MM:SS formated target time from the given 
    target_hour, target_minutes, taget_seconds.
    '''

    ## print the time in HH:MM:SS format ##

    return '{:02}:{:02}:{:02}'.format(target_hour, target_minutes, target_seconds)

if __name__ == '__main__':
    print(time_difference(3, -9))
    print(reformat_target_time(-27305.0))