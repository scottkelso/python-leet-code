def max_profit(prices: list[int]) -> int:
    max_gross = 0
    for i in range(len(prices)-1):
        future_max_price = max(prices[(i+1):])
        if future_max_price - prices[i] > max_gross:
            max_gross = future_max_price - prices[i]
    return max_gross

assert max_profit([7,1,5,3,6,4]) == 5
assert max_profit([7,6,4,3,1]) == 0



def max_profit_two(prices: list[int]) -> int:
    # sell as soon as increase in price
    max_gross = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            max_gross += prices[i+1] - prices[i]
    return max_gross


assert max_profit_two([7,1,5,3,6,4]) == 7
assert max_profit_two([1,2,3,4,5]) == 4
assert max_profit_two([7,6,4,3,1]) == 0