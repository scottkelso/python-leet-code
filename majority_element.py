def majorityElement(nums: list[int]) -> int:
    bin = dict()
    majority_value = -1
    majority_count = 0
    i = 0

    while i < len(nums):
        if nums[i] in bin:
            bin[nums[i]] += 1
        else:
            bin[nums[i]] = 1

        if bin[nums[i]] > majority_count:
            majority_value = nums[i]
            majority_count += 1
        i += 1

    return majority_value


majorityElement([2,2,1,1,1,2,2])