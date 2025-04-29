# on row 1: count freq of less than 1 between first and last non-0
# on row 2: count freq of less than 2 between first and last non-0
# on row 3: count freq of less than 3 between first and last non-0
# repeat until tallest row reached or there is only 1x column that height

# for each row
#   find first non-empty column
#   find last non-empty column
#   count gaps between non-empty columns
#   append to tally

def trap(height: list[int]) -> int:
    max_height = max(height)
    trapped = 0
    for row in range(max_height):
        trapped += trap_row(height, row)

    return trapped

def trap_row(height: list[int], row: int) -> int:
    start = 0
    end = len(height)-1

    while height[start] < 1+row:
        start += 1
    while height[end] < 1+row:
        end -= 1

    trapped = 0
    for i in range(start, end):
        if height[i] < 1+row:
            trapped += 1

    return trapped


assert trap([0,1,0,1,0]) == 1
assert trap([1,1,0,1,1,1]) == 1

assert trap([0,1,0,1,1,0,1,1,1,1,1,1]) == 2
assert trap([0,1,0,1,1,0,1,1,1,1,1,0]) == 2

assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trap([4,2,0,3,2,5]) == 9