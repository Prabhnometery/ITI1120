import random 
def getWord():
    #get random number from the list
    #can add more if needed
    myList= ["write", "program", "that", "receive", "positive", "change", "study", "excellent", "nice"]
    guess = random.randint(0,len(myList)-1)
    return myList[guess]


def playGame():
    while(True):
        #get random number
        word = getWord()
        #declare list of guess
        guessList = []
        #set all with -
        for i in range(len(word)):
            guessList.append("*");
        #get user guess
        guess = ""
        #total guess
        missedCount = 0;
        while True:
            wordMe = "";
            for w in guessList: #covering all the letter with Stars
                wordMe += w;
            guess = input("(Guess) Enter a letter in word "+wordMe+" > ")
            totalRemain =0
            found = False
            foudnInGuess = False
            for i in range(len(word)):
                if guessList[i]==guess:
                    foudnInGuess = True
                elif(word[i] == guess):
                    guessList[i] = guess
                    found = True
                if guessList[i]=='*':
                    totalRemain+=1
  
            if(not found):
                print(guess,"is not in the word")
                missedCount+=1
            elif(foudnInGuess):
                print(guess,"is already in the word")
            if totalRemain==0:
                print("Congratulation!!! you guessed",word,", You missed ",missedCount,"times")
                break
  
        choice = input("Do you want to continue again ? y or n : ")
        if(choice!='y' and choice!='Y'):
             break;
if __name__ == '__main__':
    playGame()
