weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meters : "))

BMI = weight / (height**2)
if(BMI <= 18.5):
    print("Underweight")
elif(BMI >18.5 and BMI <= 24.9):
    print("Normal weight")
elif(BMI>24.9 and BMI<=29.9):
    print("Overweight")
else:
    print("Obesity")
