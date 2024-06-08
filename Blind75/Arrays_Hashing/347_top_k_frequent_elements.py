# Time O(N), bucket sort
from collections import defaultdict
def top_k_freq2(nums, k):
    # count using hash map, key num, value count
    count_num = {}
    for n in nums:
        count_num[n] = 1 + count_num.get(n, 0)

    # key count, value num
    freq = [[] for i in range(len(nums) + 1)] # including zero
    for n, c in count_num.items():
        freq[c].append(n)

    rslt = []
    for i in range(len(nums), 0, -1):
        while len(freq[i]) > 0 and len(rslt) < k:
            rslt.append(freq[i].pop())
        if len(rslt) == k:
            return rslt
        # L16-19 could be written as  # 每加一个元素，就判别一次是否长度等于k
        # for n in freq[i]:
        #   rslt.append(n)
        #   if len(rslt) == k:
        #       return rslt


nums = [1, 2, 2, 3, 3, 3]
k = 3
print(top_k_freq2(nums, k))


# Time O(N * logN), Space O(N)
def top_k_freq(nums, k):
    '''

    :param nums: a list of numbers
    :param k: an integer to indicate the top k
    :return: a list of numbers
    '''
    count = {}
    for i in nums:
        count[i] = 1 + count.get(i, 0)
    # sort the freq
    sort_freq = sorted(count.items(), key=lambda x:x[1], reverse=True)
    rslt = []
    if k <= len(sort_freq):
        for i in range(k):
            rslt.append(sort_freq[i][0])
    else:
        for i in range(len(sort_freq)):
            rslt.append(sort_freq[i][0])

    return rslt

nums = [1,2,2,3,3,3]
k = 3
print(top_k_freq(nums, k))


# solution, Time O(N)
# Bucket Sort
# key is the frequency, value is a list of values


