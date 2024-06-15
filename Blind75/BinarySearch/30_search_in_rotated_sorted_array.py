def search(nums, target):
    start = 0
    end = len(nums) - 1

    # find the changing point index/ min index
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] > nums[start]:
            start = mid
        else:
            end = mid
    if nums[start] < nums[end]:
        min_index = start
    else:
        min_index = end

    # decide which interval to search
    if nums[start] < nums[end]:
        start, end = 0, len(nums) - 1
    elif target > nums[0]:
        start, end = 0, min_index
    elif target < nums[0]:
        start, end = min_index, len(nums) - 1
    else:
        return 0


    # after the above, we will have an ascending subarray
    while start + 1 < end:
        mid = (start + end) // 2
        if target < nums[mid]:
            end = mid
        elif target > nums[mid]:
            start = mid
        else:
            return mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1




nums = [3,4,5,6,1,2]
target = 1
print(search(nums, target))
nums = [3,5,6,0,1,2]
target = 4
print(search(nums, target))





