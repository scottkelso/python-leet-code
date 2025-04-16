def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    print(f'gas: {gas}')
    print(f'cost: {cost}')
    print([gas[i] - cost[i] for i in range(len(gas))])
    start_idx = -1
    for idx, station in enumerate(gas):
        diff = station - cost[idx]
        if diff > 0:
            print(f'found positive diff ({diff}) at station {station} (index {idx})')
            start_idx = idx - 1

    if start_idx > -1:
        new_gas = gas[start_idx:] + gas[:start_idx]
        new_cost = cost[start_idx:] + cost[:start_idx]
        print(f'new gas: {new_gas}')
        print(f'new cost: {new_cost}')
        tank = 0
        curser = 0
        while tank >= 0 and curser < len(new_gas):
            tank += new_gas[curser]
            tank -= new_cost[curser]
            curser += 1
        if curser == len(new_gas):
            return start_idx

    return -1


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
assert can_complete_circuit(gas, cost) == 3

gas = [2,3,4]
cost = [3,4,3]
assert can_complete_circuit(gas, cost) == -1
