s = input()
n = int(input())
a = []
for i in range(len(s)):
    if (i != n):
       a.append(s[i])
print(''.join(a))