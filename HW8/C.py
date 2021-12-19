print("Print your numbers")
a = map(int, input().split())
for i in a:
    if i >= 300:
        break
    elif i>=120:
        continue
    elif i % 3== 0:
        print(i)

