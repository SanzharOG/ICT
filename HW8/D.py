def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True
    
print("Enter starting number")
s = int(input())
print("Enter ending number")
e = int(input())
print("Prime numbers between " + str(s) + " and " + str(e) + " are:")
for i in range(s, e, 1):
    if(is_prime(i)):
        print(i)