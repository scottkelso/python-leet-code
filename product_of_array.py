import math

def product_except_self(nums: list[int]) -> list[int]:
    # this is O(n^2) complexity so would need to think of a way to reduce
    answer = []
    for idx, x in enumerate(nums):
        list_except_one = nums[:idx] + nums[idx+1:]
        answer.append(math.prod(list_except_one))
    return answer

assert product_except_self([1,2,3,4]) == [24,12,8,6]
assert product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]