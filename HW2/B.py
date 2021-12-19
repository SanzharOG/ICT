s = input().split()
ans = []
for i in s:
    if (len(i) % 2 == 0):
        ans.append(i)
print(' '.join(ans))
