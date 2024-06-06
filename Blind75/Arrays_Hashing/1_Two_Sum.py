# solution 1 Brute Force O(N^2)
def two_sum(nums, target):
    # N^2
    for i in range(len(nums) - 1):
        search_target = target - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == search_target:
                return [i, j]
    return []

# print(two_sum([3, 4, 5, 6], 7))
# print(two_sum([3, 4, 5], 10))

# Solution 2, Time O(n)
# def two_sum2(nums, target):
#     prev_nums = {}
#     for i in range(len(nums)):
#         diff = target - nums[i]
#         #if diff in prev_nums.keys():
#         if diff in prev_nums:     # 更有效率的写法
#             return [prev_nums[diff], i]
#         prev_nums[nums[i]] = i
#     return []

def two_sum2(nums, target):
    prev_nums = {}
    for index, value in enumerate(nums):
        diff = target - value
        #if diff in prev_nums.keys():
        if diff in prev_nums:     # 更有效率的写法
            return [prev_nums[diff], index]
        prev_nums[value] = index
    return []

print(two_sum2([3, 4, 5, 6], 7))
print(two_sum2([3, 4, 5], 10))