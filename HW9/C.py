n = int(input())
a = []
num =  [int(i) for i in input().split()]
for i in range(len(num)-2):
    if num[i] == num[i+1] or num[i] == num[i+2]:
        a.append(num[i])
    else:
        a.append(num[len(num)-1])
print(a[0])

    