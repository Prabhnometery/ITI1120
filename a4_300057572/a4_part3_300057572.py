#Family name: Prabh Simran Singh Badwal
# Student number: 300057572
# Course: IT1 1120[F]
# Assignment Number 4 Part 3


########################
# Question 1              
########################

def overlap(set1,lst1):
    '''
    (set,list)->set
    that takes a set of integers and a list of integers as parameters and that returns
    a new set containing values that appear in both structures.
    '''
    result = set()
    for num in set1:
        if num in lst1:
            result.add(num)
    return result


########################
# Question 2            
########################

def digit_sum(digit):
    '''
    (int)->(int)
    This function calculate the sum of all digits of the given integer n.

    '''

    
    if digit == 0:
        return 0
    else:
        return (digit% 10) + digit_sum(digit // 10)


def digital_root(n):
    
    if n < 10:
        return n
    else:
        return digital_root(digit_sum(n))


