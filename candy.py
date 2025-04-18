def candy(ratings: list[int]) -> int:
    length = len(ratings)
    candies_given = [1 for i in range(length)]

    for i in range(length):
        # First element
        if i == 0 and ratings[i] > ratings[i+1] and candies_given[i] <= candies_given[i+1]:
            candies_given[i] += 1

        # Middle
        if (0 < i < length-1 and
                ((ratings[i] > ratings[i+1] and candies_given[i] <= candies_given[i+1]) or
                 (ratings[i] > ratings[i-1] and candies_given[i] <= candies_given[i-1]))
        ):
            candies_given[i] += 1

        # Last
        if (i == length-1 and
                ratings[length-1] > ratings[length-2] and
                candies_given[length-1] <= candies_given[length-2]):
            candies_given[i] += 1

    return sum(candies_given)


ratings = [1,0,2]
assert candy(ratings) == 5
ratings = [1,2,2]
assert candy(ratings) == 4