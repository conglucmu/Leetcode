# Solution, O(N)
def product_of_array_sol(nums):
    rslt = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        rslt[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for j in range(len(nums)-1, -1, -1):
        rslt[j] *= postfix
        postfix *= nums[j]

    return rslt
print(product_of_array_sol([1, 2, 4, 6]))
print(product_of_array_sol([-1,0,1,2,3]))

# division, O(N)
def product_of_array(nums):
    if len(nums) == 0 or len(nums) == 1:
        return []

    non_zero_prod_all = 1
    count_zero = 0
    for n in nums:
        if n != 0:
            non_zero_prod_all *= n
        else:
            count_zero += 1
    if count_zero > 1:
        return [0] * len(nums)

    rslt = []
    for n in nums:
        if count_zero == 0:
            rslt.append(int(non_zero_prod_all/n))
        elif count_zero == 1 and n == 0:
            rslt.append(non_zero_prod_all)
        else:
            rslt.append(0)
    return rslt

print(product_of_array([1, 2, 4, 6]))
print(product_of_array([-1,0,1,2,3]))

# without division, Time O(N)
def product_of_array2(nums):
    if len(nums) == 0 or len(nums) == 1:
        return []

    # left_product = [nums[0]]
    # for i in range(2, len(nums)):
    #     left_product.append(nums[i]*left_product[i-1])
    left_product = [float('inf')] * len(nums)
    left_product[0] = nums[0]
    for i in range(1, len(nums)):
        left_product[i] = left_product[i-1] * nums[i]

    right_product = [float('inf')] * len(nums)
    right_product[len(nums) - 1] = nums[len(nums) - 1]
    for j in range(len(nums) - 2, -1, -1):
        right_product[j] = right_product[j+1] * nums[j]

    rslt = [float('inf')] * len(nums)
    rslt[0] = right_product[1]
    rslt[len(nums)-1] = left_product[len(nums)-2]
    for k in range(1, len(nums)-1):
        rslt[k] = left_product[k-1] * right_product[k+1]

    return rslt

print(product_of_array2([1, 2, 4, 6]))
print(product_of_array2([-1,0,1,2,3]))


