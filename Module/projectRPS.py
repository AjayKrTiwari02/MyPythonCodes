#Rock vs paper ->paper wins
#Rock Vs Scissor-> Rock wins
#paper vs Scissor->Scissor wins

import random

l=["rock","scissor","paper"]

while True:
    Ui=int(input('''
    STONE PAPER SCISSOR
    Press 1 to start the game ....
    Press 2 to Exit
    '''
    ))
    ccount=0
    ucount=0
    if Ui==1:
        for a in range(1,6):
            userInput=int(input('''
    Press 1 for Rock..
    Press 2 for Scissor..
    Press 3 Paper
            '''))
            if userInput==1:
                Ui="rock"
            elif userInput==2:
               Ui= "scissor"
            elif userInput==3:
                Ui="paper"
            else:
                print("Input Correct number....!")


            Cchoice=random.choice(l)
            if Cchoice==Ui:
                print("Computer Value :",Cchoice)
                print("User Value:",Ui)
                print("Draw")
                ucount=ucount+1
                ccount=ccount+1

            elif(Ui=='rock'and Cchoice=='scissor')or(Ui=='paper'and Cchoice=='rock')or (Ui=='scissor'and Cchoice=='paper'):
                print("Computer Value :",Cchoice)
                print("User Value:",Ui)
                print("You Wins")
                ucount=ucount+1
            else:
                print("Computer Value :",Cchoice)
                print("User Value:",Ui)
                print("Computer Wins")
                ccount=ccount+1
        if ucount==ccount:
            print("Game Drawn")
            print("User Score:",ucount)
            print("Computer Score:",ccount)
        elif ucount>ccount:
            print("Congratulations...!,You win the game ")
            print("User Score:",ucount)
            print("Computer Score:",ccount)
        elif ucount<ccount:
            print("Computer Wins ")
            print("User Score:",ucount)
            print("Computer Score:",ccount)
    else:
        print("ThankYou..!")
        break