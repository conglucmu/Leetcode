'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''
# Official solution:
# the same idea, Time O(m * n)
# difference: the key is (a string/list -> tuple)  rather than (a dict -> tuple)
#             the value is the list of str, not the list of index
from collections import defaultdict
def group_anagrams2(strs):
    rslt = defaultdict(list) # default value of each key is []
    for str in strs:
        count_str = [0] * 26  # assuming only lower case letters
        for l in str:
            count_str[ord(l) - ord('a')] += 1
        rslt[tuple(count_str)].append(str)
    return list(rslt.values())


# Time O(m * n), m is the length of the list, n is the length of each str
def count_letter_freq(str):
    '''
    :param str:
    :return: a sorted tuple with letter counts
    '''
    count_str = {}
    for l in str:
        count_str[l] = 1 + count_str.get(l,0)
    return tuple(sorted(count_str.items()))

def group_anagrams(strs):
    # count letter freq for each str
    group_count = []
    for str in strs:
        group_count.append(count_letter_freq(str))

    # group anagram together
    anagram_indice = {}
    for index, count in enumerate(group_count):
        if count in anagram_indice:
            anagram_indice[count].append(index)  # Learning
        else:
            anagram_indice[count] = [index]

    rslt = []
    for value in anagram_indice.values():
        rslt_each_anagram = []
        for i in value:
            rslt_each_anagram.append(strs[i])
        rslt.append(rslt_each_anagram)
    return rslt

# first attempt: typeError
# learning: # 在Python中，字典的键必须是不可变类型（immutable），
# 因为每个键都需要有一个固定的哈希值。常见的不可变类型包括整数、浮点数、字符串、元组等。
# 然而，字典（dict）本身是可变的（mutable），因此不能作为另一个字典的键。
# def count_letter_freq(str):
    '''
    output: a dict with letter counts 
    '''
#     count_str = {}
#     for l in str:
#         count_str[l] = 1 + count_str.get(l,0)
#     return count_str

# def group_anagrams(strs):
#     # count letter freq for each str
#     group_count = []
#     for str in strs:
#         group_count.append(count_letter_freq(str))
#     return group_count
#     # group anagram together
#     anagram_indice = {}
#     for index, count in enumerate(group_count):
#         if count in anagram_indice:
#             anagram_indice[count].append(index)  # Learning
#         else:
#             anagram_indice[count] = [index]
#
#     rslt = []
#     for value in anagram_indice.values():
#         rslt_each_anagram = []
#         for i in value:
#             rslt_each_anagram.append(strs[i])
#         rslt.append(rslt)
#     return rslt

strs = ["act","pots","tops","cat","stop","hat"]
# ana_index = {{'a': 1, 'c': 1, 't': 1}: 2} #typeError
print(group_anagrams(strs))
print(group_anagrams2(strs))