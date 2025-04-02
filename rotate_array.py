def rotate(nums: list[int], k: int) -> None:
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    Do not return anything, modify nums in-place instead.
    """

    print(nums)
    reversed_part = nums[-k:]
    reversed_part.reverse()
    nums = reversed_part + nums[:-k]
    print(nums)

def rotate2(nums: list[int], k: int) -> None:
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    Do not return anything, modify nums in-place instead.
    """

    for i in range(k):
        shift(nums)

def shift(nums: list[int]) -> None:
    last = nums[-1]
    for i in range(len(nums)-1):
        nums[-i-1] = nums[-i-2]
    nums[0] = last

print(rotate2([1,2,3,4,5,6,7], 3))

x = [1,2,3,4,5,6,7]
# shift(x)
rotate2(x, 3)
print(x)
