
print("Your weight")
weight = float(input())
print("Your height")
height = float(input())
bmi = round(weight/(height**2), 0)
if(bmi<18.5):
    print("Your BMI is " + str(bmi) +" you are underweight")
if(bmi>=18.5 and bmi<=25):
    print("Your BMI is " +str(bmi) +" you have a normal weight")
if(bmi >25 and bmi<=30):
    print("Your BMI is " +str(bmi) +" you are slightly overweight")
if(bmi >30 and bmi<=35):
    print("Your BMI is " +str(bmi) +" you are obese")
if(bmi >35):
    print("Your BMI is " +str(bmi) +" you are clinically obese")