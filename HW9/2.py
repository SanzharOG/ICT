s = input().split()
the = "the"
ans = []
for i in s:
    if i != the:
        ans.append(i)
print(*ans) 