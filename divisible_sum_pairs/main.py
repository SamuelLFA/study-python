# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    # Write your code here
    number_of_pairs = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                number_of_pairs += 1
    
    return number_of_pairs

# 5
print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))