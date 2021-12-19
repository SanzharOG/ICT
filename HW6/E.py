s = input()
x = 0
for i in range(len(s)):
    if(s[i] == '.'):
        x += 1
print(s.replace(".", ","))
print(x)