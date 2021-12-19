def sumOfUnique(nums):
    counts = {}
    for i in nums:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1

    uniques = [k for k, v in counts.items() if v == 1]
    return sum(uniques)  

print(sumOfUnique([int(i) for i in input().split()]))