## FAU Informatik blue tower
## the floor numbers are written in binary, giving a distinct interior look

def floor_num_from_binary(binary_floor):
    '''(str) -> (int)
    Returns the decimal floor number of the blue tower from the
    4 bit binary floor number given by binary_floor.
    '''
    dec = 0
    for i in range(len(binary_floor)):
        dec += int(binary_floor[i])*2**(len(binary_floor)-i-1)

    floor_num = dec

    return floor_num

def paint_binary(floor_num):
    '''(int) --> (str)
    Returns the 4-bit binary floor number given the
    actual floor number you are in.
    '''
    assert 0<=floor_num<=15, 'Nothing above the 15th Floor or below the Ground Floor'
    
    bits = ''
    while floor_num:
        bits += str(floor_num % 2)
        floor_num //= 2

    # if len(bits) < 4:
    #     for _ in range(4-len(bits)):
    #         bits += '0'

    binary_num = bits[::-1]

    binary_num = binary_num.zfill(4)
    return binary_num 

'''
Exercise 3.3: Pythonic binary to decimal floor conversion.
'''

def floor_num_from_binary_v2(binary_floor):
    '''(str) --> (int)
    Makes use of Python's in-built function to convert
    binary floor number to int and returns it.
    '''

    floor_num = int(binary_floor, 2)
    
    return floor_num

'''
Exercise 3.4: Pythonic decimal to binary floor conversion.
'''
def paint_binary_v2(floor_num):
    '''(int) --> (str)
    Makes use of Python's in-built function to convert
    integer valued floor number you are in and returns
    it.
    '''

	##TODO: Write your code below by removing the None and setting up your 
    # own logic. It would be more than 1 line so think carefully. ##
    assert 0<=floor_num<=15, 'Nothing above the 15th Floor or below the Ground Floor'

    binary_num = bin(floor_num)[2:]
    binary_num = '0' * (4-len(binary_num)) + binary_num 
    return binary_num


print(paint_binary(3))
print(paint_binary_v2(11))

