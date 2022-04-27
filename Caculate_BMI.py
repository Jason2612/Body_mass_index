weight = int(input("Please input your weight here: "))
height = float(input("Please input your height here: "))

BMI = weight / (height * height)

if BMI < 16:
    print("Skinny level 3")
elif BMI >= 16 and BMI < 17:
    print("Skinny level 2")
elif BMI >= 17 and BMI < 18.5:
    print("Skinny level 1")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
elif BMI >= 30 and BMI < 35:
    print("Obesity level 1")
elif BMI >= 35 and BMI < 40:
    print("Obesity level 2")
else:
    print("You need to do exercise. HURRY STAND UP!")