def can_jump(nums: list[int]) -> bool:
    if len(nums) <= 1:
        return True
    max_jump_size = nums[0]
    curser = 0
    while curser < len(nums) - 1 and max_jump_size > 0:
        curser += max_jump_size
        if curser >= len(nums):
            break
        max_jump_size = nums[curser]
        print(f'curser: {curser}, max next jump: {max_jump_size}')
    return curser == len(nums) - 1

assert can_jump([2,3,1,1,4]) == True
assert can_jump([3,2,1,0,4]) == False
