def smallest_missing_positive_integer(nums):
    nums = [num for num in nums if num > 0]
     Sort the list
    nums.sort()
    smallest_missing = 1
    for num in nums:
        if num == smallest_missing:
            smallest_missing += 1
        elif num > smallest_missing:
            return smallest_missing
    return smallest_missing
lists = [
    [3, 4, -1, 1],
    [1, 2, 0],
    [-1, -3, 4, 2]
]
for lst in lists:
    print(f"For the list {lst}, the smallest missing positive integer is {smallest_missing_positive_integer(lst)}")






    



  

