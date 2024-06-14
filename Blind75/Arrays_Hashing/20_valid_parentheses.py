def is_valid(s):
    left_stack = []
    map = {')': '(', '}': '{', ']': '['}
    for bracket in s:
        if bracket in map.values():
            left_stack.append(bracket)
        if bracket in map:
            if len(left_stack) == 0 or left_stack[-1] != map[bracket]:
                return False
            else:
                left_stack.pop()

    return len(left_stack) == 0

print(is_valid(''))
print(is_valid(']'))
print(is_valid('{'))
print(is_valid('({[([])]})'))
print(is_valid('({[([])})'))