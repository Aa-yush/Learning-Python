import random

peoples = []

while(len(peoples)<=8):
    people = input("Enter the name of a person : ")
    peoples.append(people)

selectName = random.choice(peoples)
print(selectName)
