def remove_duplicates(nums: list[int]) -> int:
    k=0
    length=len(nums)
    i=0

    while i < length-1:
        if nums[i] == nums[i+1]:
            del nums[i]
            print(f'deleting {i}')
            i-=1
            k+=1
            length-=1
        print(f'inc {i}')
        i+=1

    print(nums)
    return k


k = remove_duplicates([1,1,2])
print(f'k: {k}')

# for i in range(5):
#     print(i)
#     if i == 3:
#         i-=1
