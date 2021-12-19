def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
ans = []   
print("Enter number of terms:")
a = int(input())
print("Fibonacci sequence:")
for i in range(a):
  ans.append(fibonacci(i))
print(*ans)