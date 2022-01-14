import random

def gameWin(comp,you):
    if comp == you:
       return None
    elif comp == 's':
        if you =='w':
            return False
        elif you =='g':
            return True
    elif comp == 'w':
        if you =='g':
            return False
        elif you=='s':
            return True

    elif comp =='g':
        if you=='w':
            return True
        elif you =='s':
            return False


while True: 
    # print("Computer Turn: Snake (1) Water (2) Gun (3) ?")
    randNO = random.randint(1,3)
    # print(randNO)

    if randNO ==1:
        comp = 's'
    elif randNO ==2:
        comp = 'w'
    else:
        comp ='g'

    you = input("Your Turn: Snake (s) water (w) Gun (g) Exit(e) ? ")
    if you=='e':
        break
    elif you !='s' and you != 'w' and you !='g' and you !='e':
        print("Incorrect  option !!!!!! ")
        continue
       
    a = gameWin(comp ,you)
    print(f"You chose {you} : computer chose {comp}")
    if a== None:
        print("Tie!")
    elif a:
        print("You Win!")
    else:
        print("You Lose!")