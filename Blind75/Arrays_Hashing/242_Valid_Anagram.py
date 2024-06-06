# Solution 1: Time O(N), Space O(N)
def is_anagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    dict_s = count_letters(s)
    dict_t = count_letters(t)

    return dict_s == dict_t

# def count_letters(s):
#     dict_s = {}
#     for l in s:
#         if l in dict_s.keys():
#             dict_s[l] += 1
#         else:
#             dict_s[l] = 1
#     return dict_s


# solution 2: simpler version of Solution 1
# Learning: easier way by using dict.get()
def count_letters(s):
    countS = {}
    for l in s:
        countS[l] = 1 + countS.get(l, 0)
    return countS


print(is_anagram(s = "racecar", t = "carrace"))
print(is_anagram('jar', 'raj'))
print(is_anagram('abc', 'aed'))



# Solution 3: Time O(N logN), Space O(1)
# Learning: syntax of sorting a string
def is_anagram2(s, t):
    return sorted(s) == sorted(t)

print(is_anagram2(s = "racecar", t = "carrace"))
print(is_anagram2('jar', 'raj'))
print(is_anagram2('abc', 'aed'))