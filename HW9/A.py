numbers = [int(i) for i in input().split()]
cnt=0
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if i == j:
            continue
        if numbers[i] == numbers[j]:
            cnt+=1
    
print(cnt)