def max_area(height: list[int]) -> int:
    max_area_overall = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            y_height = min(height[i], height[j])
            x_distance = j - i
            area = y_height * x_distance
            if area > max_area_overall:
                max_area_overall = area
    return max_area_overall


assert max_area([1,1]) == 1
assert max_area([1,8,6,2,5,4,8,3,7]) == 49