# Solution T: O(N), S: O(N)
def longest_consecutive(nums):
    set_nums = set(nums)
    longest = 1

    for n in set_nums:
        if (n-1) not in set_nums:
            length = 1
            cur = n
            while cur + 1 in set_nums:
                length += 1
                cur += 1
            longest = max(length, longest)

    return longest

nums = [2,20,4,10,3,4,5]
print(longest_consecutive(nums))

nums = [0, -1]
print(longest_consecutive(nums))



# T: O(N)  S: O(N)
def longest_consecutive(nums):
    set_nums = set(nums)
    count_final = 0
    count = 1

    while len(set_nums) != 0:
        k = set_nums.pop()
        cur = k
        while cur + 1 in set_nums:
            count += 1
            cur += 1
            set_nums.discard(cur)

        cur = k
        while cur - 1 in set_nums:
            count += 1
            cur -= 1
            set_nums.discard(cur)

        count_final = max(count, count_final)
        count = 1

    return count_final
nums = [2,20,4,10,3,4,5]
print(longest_consecutive(nums))

nums = [0, -1]
print(longest_consecutive(nums))

