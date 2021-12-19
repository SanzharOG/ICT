print("Input your number")
a = int(input())
sum = 0
for i in range(1, a+1, 1):
    sum +=i
print("Sum of firts " + str(a) +" numbers is: " + str(sum))
print("Average of firts " + str(a) +" numbers is: " + str(sum/a))