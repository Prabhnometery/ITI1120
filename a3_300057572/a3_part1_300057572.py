#Family name: Prabh Simran Singh Badwal
# Student number: 300057572
# Course: IT1 1120
# Assignment Number 3


########################
# Question 1               
########################
def coprime(x, y):
    '''
    (int,int)->bool
    Precondition: x and y are both positive integers

    >>> coprime(1,7)
    True
    >>> coprime(21,14)
    False
    >>> coprime(14,15)
    True
    >>> coprime(7,7)
    False
    
    '''
    
    for i in range(2, x+1):
        if x % i == 0 and y % i == 0:
            return False
    return True
    

########################  
# Question 2
########################

def all_coprime_pairs(l):
    """
    (list)->(list)
    This fuction takes a list of integers as input and returns a list of pairs of coprime numbers by calling the function coprime
    """
    t=len(l)
    b=[]
    for i in range(t-1):
        for j in range(i+1,t):
            a=coprime(l[i],l[j])
            if a==True:
                b.append((l[i],l[j]))
    return b


########################  
# Question 3   
########################
def zero_out(a1,a2):
    '''
    (list, list) -> list
    If a2 is a subset of a1, a1 is returned with the subset elements
    replaced by 0s. 
    Precondition: a2 must be smaller than a1; a1 and a2 have a length
    
    '''  

    if len(a1) < len(a2):
            return None
    
    # check the start of possible combination in
    # list a1
    i = 0
    while i < (len(a1) - len(a2) + 1):
            
            sublist = a1[i:(i + len(a2))]
            if sublist == a2:
                    for x in range(len(a2)):
                            a1[i+x] = 0
                    i += len(a2)
            else:
                    i += 1
    return a1

########################  
# Question 4    
########################
def coin_flip(filename):
    '''
        (file) -> None
        Prints "You win!" if the number of heads are flipped more than 50 percent.
        Precondition: The file must contain at least one space between each letter    
    '''
    infile = open(filename)
    llist = []
    for f in infile.readlines():
        llist.append(f)
    for data in llist:
        count = 0
        total = 0
        data = data.rstrip('\n')
        ll = data.split(' ')

        for ch in ll:
            if len(ch) > 0:
                if ch == 'h' or ch=="H":
                    count += 1
                total = total + 1

                print(str(count) + " Heads " , end = "")
                per = count*100/total
                print(round(count*100/total,2), "%")
                if per>50:
                    print("You Win!")

    infile.close()



########################  
# Question 5 (DONE)
########################

import random

def throwDice():
        return random.randint(1, 6)

def Run():
        seq = [str(throwDice()) for _ in range(20)] # _ used for storing values not that wont be used again

        # try to group the values now.
        # convert single list to nested list.
        groupedList = [[seq[0]]]

        for i in range(1, len(seq)):
                current = seq[i]
                if current == groupedList[-1][-1]:
                        groupedList[-1].append(current)
                else:
                        groupedList.append([current])

        #print(groupedList)
        results = []  
        for x in groupedList:
                if len(x) > 1:
                        results.append('(' + ' '.join(x) + ')')
                else:
                        results.append(x[0])
        
        print(' '.join(results))



########################  
# Question 6 
########################
import random
def craps():
    
    '''
    (None) -> int
    Returns 1 if the plaer wins and 0 if the player loses. The player wins if
    she rolls a total of 7 or 11; the player loses if she rolls a total of 2,
    3 or 12. 
    Precondition: None
    
    '''

    ind1 = random.randint(1,6)
    ind2 = random.randint(1,6)
    indSum = ind1 + ind2
    if indSum == 7 or indSum == 11:
        return 1
    elif indSum == 2 or indSum == 3 or indSum == 12:
        return 0
    else:
        while True:
             ind1 = random.randint(1,6)
             ind2 = random.randint(1,6)
             temp = ind1 + ind2
             if temp == 7:
                 return 0
             elif temp == indSum:
                 return 1
def testCraps(n):
    count = 0
    for i in range(n):
        if craps() == 1:
            count += 1
    return count/n

########################
# Question 7 
########################

def is_all_even(lis):
    '''
    (2D-list) -> bool
    Returns True if all the elements in lst are even
    Precondition: None 
    ''' 

    if len(lis) == 0:
        return True
    
    
    for i in range(len(lis)): 
        for j in lis[i]: 
            if j%2 != 0:
                return False
    return True

########################  
# Question 8 
######################## 

def range_(lis):    # I used rangeL insetead of range becuase range is a pre-defined function and it corrupts entire code where we use rang
    
    if lis is None or len(lis) == 0:
        return 0

    minimum = lis[0][0]
    maximum = lis[0][0] 
    for i in lis: #entering the list
        for num in i: #entering the inner list 
            if num > maximum: 
                maximum = num
            if num < minimum:
                minimum = num
    return maximum - minimum +1








        
 

         
            

        

    

                
    
                
                 
     
