nums = [0,1,2,2,3,0,4,2]

i=2

for j in range(i, len(nums)-1):
    nums[j] = nums[j+1]


print(nums)