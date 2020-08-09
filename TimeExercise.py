import matplotlib.pyplot as plt
import time as t

print("This program is used to improve your typing speed. Enter 'Programming word 5 times'")
input("Press Enter to continue..")


times = []
mistake = 0

for x in range(0,5):
    start_time = t.time()
    word = input("Enter the word: ")
    end_time = t.time()

    time_elapsed = end_time - start_time


    times.append(time_elapsed)

    if(word.lower()!="programming"):
        mistake = mistake+1;

print("You made ",mistake," mistake(s)")
print("Now Let's see your evolution")
t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,times)
plt.show()


        




        
