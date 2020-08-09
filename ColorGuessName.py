import random
colors = ["red","yellow","pink","green","blue"]

chooseColor = random.choice(colors)
flag = True

while flag:
    guessColor = input("Enter your guess color name : ").lower()
    if(guessColor == chooseColor):
        print("Yes , Your guessing is right")
        break
    else:
        response=input("No , Your guessing is not right . Do you want to continue ? (yes/no) : ").lower()
        if(response=="no"):
            flag=False
        elif(response=="yes"):
            flag=True
        else:
            flag=False
        
