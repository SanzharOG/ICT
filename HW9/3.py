print("your age?")
age = int(input())
print("your gender?")
gen = input()    
print("your marital status?")
mar = input()
if gen =="F" and age >= 20 and age <= 60:
    print("work only in urban areas")
elif gen == "M" and age >=20 and age <=40:
    print("may work in anywhere")
elif gen == "M" and age > 40 and age <=60:
    print("work in urban areas only")
else:
    print("ERROR")
    