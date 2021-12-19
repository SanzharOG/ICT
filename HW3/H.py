print("age of first people")
f = int(input())
print("age of second people")
s = int(input())
print("age of third people")
t = int(input())
if(f>=s and f>=t):
    print("first is the oldest")
elif(s>=f and s>=t):
    print("second is the oldest")
elif(t>=f and t>=s):
    print("third is the oldest")
if(f<=s and f<=t):
    print("first is the most young")
elif(s<=f and s<=t):
    print("second is the most young")
elif(t<=f and t<=s):
    print("third is the most young")