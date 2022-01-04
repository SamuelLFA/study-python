# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    # Write your code here
    number_ways = 0
    for i in range(len(s) - (m-1)):
        to_evaluate = s[i:i+m]
        if sum(to_evaluate) == d:
            number_ways += 1
    return number_ways

# 2
print(birthday([1, 2, 1, 3, 2], 3, 2))
# 0
print(birthday([1, 1, 1, 1, 1, 1], 3, 2))
# 1
print(birthday([4], 4, 1))