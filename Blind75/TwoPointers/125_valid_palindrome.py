def is_palindrome(s):
    if not s:            # '' 空string 需要定义，否则会报错
        return True
    s_lower = s.lower()
    left = 0
    right = len(s_lower) - 1
    letters = 'abcdefghijklmnopqrstuvwxyz1234567890'

    while left + 1 < right: #
        if s_lower[left] not in letters:
            left += 1
        if s_lower[right] not in letters:
            right -= 1
        if s_lower[left] in letters and s_lower[right] in letters:
            if s_lower[left] != s_lower[right]:    # 先后次序很重要，不能先移动pointer 再判断
                return False
            if s_lower[left] == s_lower[right]:
                left += 1
                right -= 1
    if left == right:
        return True
    if s_lower[left] in letters and s_lower[right] in letters:
        return s_lower[left] == s_lower[right]
    else:        # 结束的时候corner case： 最中间的两个不全是letter or number
        return True


s = "A man, a plan, a canal: Panama"
s = 'race a car'
s = ''
print(is_palindrome(s))



