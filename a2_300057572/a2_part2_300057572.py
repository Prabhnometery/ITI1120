######################
#### Midterm-1 #######
######################
def midterm1():
    print("Midtem 1: ")
    weight1 = int(input("Weight (0-100)? "))
    score1 = int(input("Score earned? "))
    is_score_shifted1= int(input("Were scores shifted (1=yes, 2=no) ? "))
    if is_score_shifted1 == 1:
        shift1 = int(input("Score shift ? "))
        add = score1+shift1
        if add >= 100:
            print("Total points = 100 / 100")
            print("Weighted score = "+str(float(weight1))+" / "+str(weight1))
            return weight1
        else:
            print("Total points = "+str(add)+" / 100")
            print("Weighted score = "+str(float(weight1))+" / "+str(weight1))
            return (add*weight1)/100
    else:
        weighted_score1 = (weight1*score1)/100
        print("Total points = "+str(score1)+" / 100")
        print("Weighted score = "+str(round(weighted_score1,1))+ " / "+str(weight1))
        return weighted_score1

######################
#### Midterm-2 #######
######################

def midterm2():
    print()
    print("Midtem 2: ")
    weight2 = int(input("Weight (0-100)? "))
    score2 = int(input("Score earned? "))
    is_score_shifted2= int(input("Were scores shifted (1=yes, 2=no) ? "))
    if is_score_shifted2 == 1:
        shift2 = int(input("Score shift ? "))
        add = score2+shift2
        if add >= 100:
            print("Total points = 100 / 100")
            print("Weighted score = "+str(float(weight2))+" / "+str(weight2))
            return weight2
        else:
            print("Total points = "+str(add)+" / 100")
            print("Weighted score = "+str(float(weight2))+" / "+str(weight2))
            return (add*weight2)/100
    else:
        weighted_score2 = (weight2*score2)/100
        print("Total points = "+str(score2)+" / 100")
        print("Weighted score = "+str(round(weighted_score2,1))+" / "+str(weight2))
        return weighted_score2
        
######################
#### Final #######
######################
    
def final():
    print()
    print("Final: ")
    weightf = int(input("Weight (0-100)? "))
    scoref = int(input("Score earned? "))
    is_score_shiftedf= int(input("Were scores shifted (1=yes, 2=no) ? "))
    if is_score_shiftedf == 1:
        shiftf = int(input("Score shift ? "))
        add = scoref+shiftf
        if add >= 100:
            print("Total points = 100 / 100")
            print("Weighted score = "+str(float(weightf))+" / "+str(weightf))
            return weightf
        else:
            print("Total points = "+str(add)+" / 100")
            print("Weighted score = "+str(float(weightf))+" / "+str(weightf))
            return (add*weightf)/100
    else:
        weighted_final = (weightf*scoref)/100
        print("Total points = "+str(scoref)+" / 100")
        print("Weighted score = "+str(round(weighted_final,1))+" / "+str(weightf))
        return weighted_final

######################
#### Homework ########
######################
    
def homework():
    print()
    list1 = []
    list2 = []
    print("Homework:")
    homework_weight=int(input("Weight(0-100)? "))
    no_of_assign=int(input("Number of assignments? "))
    for i in range(1,no_of_assign+1):
        assign_score=int(input("Assignment "+str(i)+" score? "))
        assign_max=int(input("Assignment "+str(i)+" max? "))

        list1.append(assign_score)
        list2.append(assign_max)
      
    sections=int(input("Number of sections attended? "))
    print("Section points = "+str(sections*3)+" / 34")

    if (sum(list1)+(sections*3)) >= (sum(list2)+34): 
        print('Total points = '+str(34 + sum(list2))+' /'+str(34 + sum(list2)))
        print('Weighted score = '+str(homework_weight)+' /'+str(homework_weight))
        return homework_weight
    else:
        weighted_score = ((sum(list1) + (sections*3))*homework_weight)/(34 + sum(list2))
        print('Total points = '+str(sum(list1)+(sections*3))+' / '+str(34 + sum(list2)))
        print('Weighted score = '+str(round(weighted_score,1))+' / '+str(homework_weight))
        return round(weighted_score,1)

######################
#### Quizzes #########
######################

def quizzes():
    print()
    print("Quizzes: ")
    quizzes_weight = int(input("Weight (0-100)? "))
    quizzes_scores = int(input("Total points earned? "))
    quizzes_max = int(input("Total points possible? "))
    weighted_quizzes = (quizzes_scores*quizzes_weight)/quizzes_max
    print("Total points = "+str(quizzes_scores)+" / "+str(quizzes_max))
    print("Weighted score = "+str(round(weighted_quizzes,1))+" / "+str(quizzes_weight))
    return round(weighted_quizzes,1)
    
######################
#### Daily Homework ##
######################

def daily_homework():
    print()
    print("Daily homework: ")
    d_weight = int(input("Weight (0-100)? "))
    d_scores = int(input("Total points earned? "))
    d_max = int(input("Total points possible? "))
    weighted_d = (d_scores*d_weight)/d_max
    print("Total points = "+str(d_scores)+" / "+str(d_max))
    print("Weighted score = "+str(round(weighted_d,1))+" / "+str(d_weight))
    return round(weighted_d,1)

######################
#### Grades ##########
######################

def grades(x):
    if x >= 90:
        return 'A'
    elif 80<=x<=90:
        return 'B'
    elif 70<=x<=80:
        return 'C'
    elif 60<=x<=70:
        return 'D'
    else:
        return 'F'

######################
#### Main ##########
######################
    
print("This program reads exam/homework scores and reports your overall course grade.")   
overall_percentage= round((midterm1()+midterm2()+final()+homework()+quizzes()+daily_homework()),1)
print()
print("Overall Percentage = "+str(overall_percentage))

which_grade = grades(overall_percentage)
print("Your grade will be at least: "+str(which_grade))
if which_grade == 'A':
        print("<< Your limitation—it's only your imagination ! >>")
elif which_grade == 'B':
        print("<< Great ! Always be a constant learner. >>")
elif which_grade == 'C':
        print("<< Hardwork beats talent when talent doesn't work hard ! >>")
elif which_grade == 'D':
    print("<< Never Stop Trying ! >>")
elif which_grade == 'F':
        print("<< Failure is a stepping stone to Success ! >>")


    

    
    



    
    
   




