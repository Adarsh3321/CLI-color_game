import random
import subprocess



print("welcome to color game")
color=["red","green","blue","black","white"]
attempt =5
loss =0
win=0
def sgame():
    global attempt
    global win
    global loss
    valid=False
    m_choice=random.choice(color)
    if attempt<=0:
        print("out of attempts\n")
        next=int(input("1> to see scoreboard\n2> to play again\nanything else to exit"))
        if next==1:
            print("name :",name,"\ngame won = ",win,"\n \nGame lost = ",loss,"\nyour accuracy :",(win/5)*100)
        if next==2:
            subprocess.run(["python","pc.py"])
        else:
            return
        return
    
    
    u_choice=input("enter color : ")
    
    for i in color:
        if u_choice == i:
            valid=True
            break

    if valid:
    
        if m_choice==u_choice:
            print("you won")
            attempt-=1
            win+=1
            print(attempt,"left of 5")
            sgame()
        else:
            print("you lost try again")
            loss+=1
            attempt-=1
            print(attempt,"left of 5")
            sgame()

    else:
        print("invalid entry try again")
        sgame()
    return
name=input("enter your name : ")
game=int(input("enter 1 to start 2 to exit : "))
if game == 1:
    sgame()



































"""
Welcome to the color game>>>
please enter the name for score board

1> start game
2> exit

if 1
please enter the color: redasddfa
 validate the color if the given color is not present in the
 list then tell user you have entered invalid color

 if color is validated then
 match it with machine generated color
 if matching then display the message like
 you wom the game
 number of attempts : 1
 total number of attempts: 5

 if not matching then display the message:

 your guess was wrong please try again
 number of attempts left: 04

 once after completing the game till 5th attempts tell user
 1> see score board
 2> play again
 3> exit

 if he  choose 1 then:
 number of game won:01
 number of game loose:01
 name of the player: abc
  
"""