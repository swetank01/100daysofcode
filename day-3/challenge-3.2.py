# BMI 2.0

height=float(input("Enter your Height:(m) "))
weight=float(input("Enter your Weight:(kg) "))

bmi = int(weight/(height ** 2))

if bmi < 18.5:
    print(f"your bmi is {bmi} and you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi} and you have normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi} and you are overweight")
elif bmi < 35:
    print(f"your bmi is {bmi} and you are obese")
else:
    print("your bmi is {bmi} and your are clinically obese")