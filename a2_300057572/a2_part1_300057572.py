#Family name: Prabh Simran Singh Badwal
# Student number: 300057572
# Course: IT1 1120[F]
# Assignment Number 2 Part-1

########################
# Question 1               
########################
def print_factors(n):
    
    '''
    Pre-conditon = n should be a non zero number
    (int)->None,bool
    This function takes an integer n as a parameter and prints out all the factors of n,
    returning True if 2 is a factor of n and returning False otherwise.

    '''    
    print("factors of "+str(n)+" =",end=' ')
    
    for i in range(1,n+1):
        if n%i == 0:
            print(i,end= ' ')
    return n%2 == 0

########################
# Question 2            
########################
def triangle(n):
    
    '''
    (int)->None
    This function takes an integer size as a parameter and prints a size * 2 – 1 wide by size
    tall triangle of numbers.
    

    '''
    wide = 2*n - 1
     
    if n > 0:
        for i in range(1, n + 1):
            for j in range(1, wide+1):
                if i <= j <= 2*n-i:
                    print(j%10, end='')
                else:
                    print(end=' ')
            print()
        
########################
# Question 3             
########################

def approxPi(x):
    
    '''
    (int)->(float)
    This function takes input a float-value error and approximates constant π within error by computing the preceding
    sum, term by term, untilthe difference between the current sum and the previous sum (with one less term)
    is no greater than error.

    '''
    
    prev = 0 
    csum = 0 
    den = 1 
    diff = 0 
    term = "even" 
    while True:
       if term == "even":
           csum += 4/den
           term = "odd" 
           diff = csum - prev
       elif term == "odd":
           csum -= 4/den
           term = "even" 
           diff = prev - csum
       den += 2
       if diff <= x: 
           return csum
       prev = csum
       

########################
# Question 4             
########################

def is_fib_like(numbers):
    
    '''
    (lst)->bool
    This function takes a list of integers as a parameter and that returns whether or not
    the sequence matches the pattern of the Fibonacci sequence (True if it does, False if it does not)

    '''
    
    if len(numbers) <= 2:
        return True
    
    last1 = numbers[0]
    last2 = numbers[1]

    for x in numbers[2:]:
        if x != last1 + last2:
            return False

        last1 = last2
        last2 = x

    return True

########################
# Question 5            
########################

def longest_name(n):
    
    '''
    (str)->None
    This function reads names typed by the user and prints the longest name.
    
    '''
    b = []
    list1 =[]
    count = 0
    for i in range(1,n+1):
        a = input("name #"+str(i)+"? ").lower().strip()

        c = b.append(a) 
    for j in b:
        if len(j) > count:
            count += len(j)
            word = j
            d = list1.append(j)
    print(word.capitalize()+"'s name is longest")
    
    if len(b)>5:
        print("(There was a tie!)")
        
########################
# Question 6             
########################
def encrypt(x,y):
    
    '''
     (str,str)->(str)
    
     This function takes as input a 10-digit string key and a digit string
     (i.e., the clear text to be encrypted) and returns the encryption of the clear text.
     
    '''
    string = ""
    for i in range(len(y)):
        string += x[int(y[i])] #index = int(y[i])
    return string





            
        
    



        
    
    


    
