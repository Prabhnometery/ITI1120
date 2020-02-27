#Family name: Prabh Simran Singh Badwal
# Student number: 300057572
# Course: IT1 1120[F]
# Assignment Number 2 Part 1

########################
# Question 1a          
########################

def largest_34(a):
    '''
    (list)->(int)
    This function returns the sum of the 3rd and 4th largest valuesin the list a
    Pre-Condition - The list a has at least 4 elements

    '''
    sort_a = a.sort()
    l = len(a)-1

    sum_of_34 = a[l-2] + a[l-3]
    return sum_of_34


########################
# Question 1b       
########################

def largest_third(a):
    '''
    (list)->(int)
    
    Pre-Conditon - The numbers in the list a are all distinct
    and that the list a has at least 3 elements.
    
    This function computes the sum of the len(a)//3 of the largest values in the list a.
    '''
    
    a.sort()
    count = 0

    for i in range(len(a)-1,len(a)//3+1,-1):
        count += a[i]
    return count 
        

    
#largest_third([3,1,6,8,10,9,2])


########################
# Question 1c    
########################

def third_at_least(a):
    '''
    (list)->(int)
    This function returns a value in a that occurs at least len(a)//3 + 1 times
    
    '''
    b=a
    for i in range(len(b)):
        count = 0
        for j in range(len(b)):
            if b[i]==b[j]:
                count += 1
        if(count >= len(b)//3 + 1):
            return b[i]
        return None 


########################
# Question 1d      
########################
def sum_tri(a,x):
    
       '''
    (list,int)->bool
    This function takes a list , a, as input and returns True if there exists
    indices i, j and k (where i and j and k are not necessarily distinct)

    '''
     
       for i in range(len(a)):
           for j in range(len(a)):
               for k in range(len(a)):
                   if(a[i]+a[j]+a[k]==x):
                       return True
       return False

    


    

    
    
