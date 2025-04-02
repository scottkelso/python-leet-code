def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    tempNums = []

    m = m - 1
    n = n - 1

    while m >= 0 and n >= 0:
        print(f'm:{m}, n:{n}')
        if nums1[m] >= nums2[n]:
            print(f'Adding {nums1[m]} from nums1')
            tempNums.append(nums1[m])
            m = m - 1
        else:
            print(f'Adding {nums2[n]} from nums2')
            tempNums.append(nums2[n])
            n = n - 1

    while m >= 0:
        tempNums.append(nums1[m])
        m -= 1

    while n >= 0:
        tempNums.append(nums2[n])
        n -= 1
    nums1 = tempNums[::-1]
    print(tempNums[::-1])

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print()
