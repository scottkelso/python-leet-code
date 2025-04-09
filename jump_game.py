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


def can_jump_two(nums: list[int]) -> int:
    if len(nums) <= 1:
        return 0
    max_jump_size = nums[0]
    curser = 0
    jumps = 0
    while curser < len(nums) - 1 and max_jump_size > 0:
        if curser >= len(nums):
            break
        max_jump_size = nums[curser]

        if max_jump_size < 2:
            curser += max_jump_size
        else:
            # choose largest num within jump range
            one_step = curser+1
            can_jump_to = nums[one_step:one_step+max_jump_size]
            largest_next_jump_idx = can_jump_to.index(max(can_jump_to))
            curser += largest_next_jump_idx + 1
        jumps += 1
        print(f'curser: {curser}, max next jump: {max_jump_size}')
    return jumps

assert can_jump_two([2,3,1,1,4]) == 2
assert can_jump_two([2,3,0,1,4]) == 2
assert can_jump_two([2,2,3,1,4]) == 2
assert can_jump_two([4,2,3,1,4]) == 1
assert can_jump_two([1,1,1,1,4]) == 4
