def find_min(nums):
    '''
    [4, 5, 6, 1, 2, 3]

    :param nums:
    :return:
    '''

    if not nums:
        return None
    # rotated 6x times
    if nums[0] < nums[len(nums) - 1]:
        return nums[0]

    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] > nums[start]:
            start = mid
        else:
            end = mid

    return min(nums[start], nums[end])

print(find_min([3,4,5,6,1,2]))
print(find_min([4,5,0,1,2,3]))
print(find_min([4,5,6,7]))

