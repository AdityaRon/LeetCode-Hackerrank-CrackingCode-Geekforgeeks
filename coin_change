def coin_change(target,coins):
    known_list = [0] + (target) * [float('Inf')]
    for coin in coins:
        for i in range(coin, target+1):
            known_list[i] = min(known_list[i],known_list[i-coin]+1)
    print(known_list)
    return (known_list[-1] if known_list[-1] != float('inf') else -1)
