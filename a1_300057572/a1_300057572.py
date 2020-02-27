# Family name: Prabh Simran Singh Badwal
# Student number: 300057572
# Course: IT1 1120
# Assignment Number 1


########################
# Question 1               
########################

def repeat(string, n, delim):
    ''' 
    This function returns the string string
    repeated n times, separated by the string delim.

    '''

    print('"'+(string+delim)*(n)+'"')

########################  
# Question 2
########################

def is_prime(x):
    
    ''' (int)->(bool)
    This function returns a boolean value indicating whether an integer is prime or not.
    '''
    
    if x == 2:
        return True 
    
    for i in range(2,x):
        if x%i == 0:
            return False
        else:
            return True

########################  
# Question 3
########################       
    
def points(x1,y1,x2,y2):
    
    ''' (int)->(none)
    This function takes as input four numbers x1, y1, x2, y2 that are the coordinates of two points (x1;y1) and (x2; y2) in the plane and computes
    a. The slope of the line going through the points, unless the line is vertical
    b. The distance between the two points.

    '''
    
    slope = (x2-x1)/(y2-y1)
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

    if x1 == x2:
       print("The slope is infinty and the distance is "+str(distance))
    else:
       print("The slope is "+str(1/slope)+" and the distance is "+str(distance))


########################  
# Question 4    
########################       

def month_apart(m1,d1,m2,d2):
    ''' (int)->(bool) '''
    
    return (m1-m2 > 1) or (m2-m1 > 1) or (m2-m1 == 1 and d2>=d1) or (m1-m2 == 1 and d1>=d2)

########################  
# Question 5
########################      

def reverse_int(x):
    
    ''' (int)->(int)
    This function takes a three-digit integer as input and returns the integer obtained by reversing its digits.

    '''

    c = x%100 
    f = x//100
    d = c//10 
    e = c%10   

    return e*100 + d*10 + f

########################  
# Question 6
########################

def vowelCount(x):
    ''' (str)->(none)
    This function takes a string as input and counts and prints the number of occurrences of vowels in the string.

    '''

    
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    
    s = x.lower()
    for i in s:
        if i in 'a':
            count_a += 1
        elif i in 'e':
            count_e += 1  
        elif i in 'i':
            count_i += 1   
        elif i in 'o':
            count_o += 1     
        elif i in 'u':
            count_u += 1
    print(f"a, e, i, o, and u appear, respectively, {count_a}, {count_e}, {count_i}, {count_o}, {count_u} times.")
            


########################
# Question 7(a)
########################

def allTheSame(x, y, z):
    ''' This function returns true if the arguments are all the same.'''
    return x == y == z


########################
# Question 7(b)
########################

def allDifferent(x, y, z):
    ''' This function returns true if the arguments are all different.'''
    return x != y != z

########################
# Question 7(c)
########################
def sorted(x, y, z):
    ''' This function returns true if the arguments are sorted, with the smallest one coming first '''
    
    return x < y < z

########################  
# Question 8
######################## 

def leap(x):

    ''' (int)->(bool)
    This function takes one input argument—a year—and returns True if the year is a leap year and False otherwise.

    '''

    return (x%4 == 0 or x%400 == 0) and (x%100 != 0 or x%400 == 0)
        


########################
# Question 9    
########################

def letter2number(x):
   '''
       (str)->(int)
       This function takes as input a letter grade (A, B, C, D, F, possibly with a - or +) and returns the corresponding number grade.
   '''
   
   grades = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0};
  
   
   if len(x) > 1:
      
       if x[1] == '+':
           return grades[x[0]] + 0.3;
       elif x[1] == '-':
           return grades[x[0]] - 0.3;
       else:
           return grades[x[0]];
   elif len(x) == 1:
       return grades[x[0]];


########################  
# Question 10
########################

def is_palindrome(x):

    ''' (str)->(bool)
    This function accepts a string as argument and returns True or False indicating whether the string is a palindrome or not.

    '''
    
    for i in x:
        if x[0] == x[len(x)-1]:
            return True
        else:
            return False
        
########################  
# Question 11
########################

def is_nneg_float(x): #(last example error)
    ''' (str)->(bool)
    This function returns True if string contains (at most) one decimal point and one or more digits (and nothing else); and False otherwise.

    '''

    for i in x:
        if i in '.':
            return True
        elif i in '-e':
            return False
        else:
            return True 
          

########################  
# Question 12
########################

def rps(p1,p2):
    ''' (str)->(int)
    This function takes the choice ('R', 'P', or 'S') of player 1 and the choice of player 2, and returns -1 if player 1 wins, 1 if player 2 wins, or 0 if there is a tie.

    '''
    
    if (p1 == 'R' and p2 == 'S') or (p1 == 'P' and p2 == 'R') or (p1 == 'S' and p2 == 'P'):
        return -1
    elif (p1 == p2):
        return 0
    else:
         return 1


########################  
# Question 13 
########################

import math

def alogical(num):
    ''' (number)->int
    Returns the number of times n can be divided by 2 before we get something <=1
    Thus you need to solve n/(2*2*2 ...)=n/(2**x) <= 1 equation for x.
    That is a definition of log base 2 of n, log_2 n '''

    return math.ceil(math.log2(num))


########################  
# Question 14
########################

def count_even_digits(x,y):
    
    ''' (int)->(int)
    This function accepts two integers as parameters and returns the number of even-valued digits in the first number

    '''
    count = 0
    num = str(x)
    for i in num:
        if int(i)%2 == 0:
            count += 1
    return count
        







        
 
