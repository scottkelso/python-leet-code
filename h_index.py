def h_index(citations: list[int]) -> int:
    citations.sort(reverse=True)
    h=0
    while True:
        if citations[h] >= h+1: h+=1
        else: break
    print(h)
    return h

assert h_index([3,0,6,1,5]) == 3
assert h_index([1,3,1]) == 1
