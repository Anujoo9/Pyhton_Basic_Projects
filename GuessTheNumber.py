import random
randNumber = random.randint(1,100)
print(randNumber)
Guess = 1
user = int(input("Guess a number between 1 and 100 "))
while(True):
    if (user == randNumber):
        print(f"You guessed it right, and number of Guess are {Guess}")
        break
    if(user > randNumber):
        user = int(input("You guessed it Wrong!, Enter small number "))
        
    else:
        user = int(input("You guessed it Wrong!, Enter a big number "))

    Guess+=1# here Guess will increase in each case

with open ("hiscore.txt","r") as x:
    hs = int(x.read())

if(Guess<hs):
    print("You have just Broken HighScore")
    with open ("hiscore.txt","w") as f:
        f.write(str(Guess))
else:
    print(f"Previous high Score is {hs}")
