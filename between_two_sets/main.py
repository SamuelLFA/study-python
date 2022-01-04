# https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    # Write your code here
    totalX = 0
    is_valid = True
    for item_to_avaliate in range(a[0], b[-1] + 1):
        is_valid = True
        for item in a:
            if item_to_avaliate % item != 0:
                is_valid = False
                break
        for item in b:
            if item % item_to_avaliate != 0:
                is_valid = False
                break
        if is_valid is True:
            totalX += 1
    return totalX

# 3
print(getTotalX([2, 4], [16, 32, 96]))
