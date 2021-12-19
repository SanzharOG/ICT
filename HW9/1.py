s = input()
n = int(input())
ans = []
for i in range(len(s)):
    if i<n and (ord((s[i]))>=97 and ord(s[i])<=122) or (ord((s[i]))>=60 and ord((s[i]))<=90):
        ans.append(s[i])
        
for i in range(n,len(s),1):
    ans.append(s[i])

print("".join(ans))