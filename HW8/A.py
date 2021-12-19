print("Input your number")
a = int(input())
b = []
for i in range(a, 0, -1):
    b.append(i)
for i in range(0, len(b), 1):
    print(*b)
    b.pop(0)