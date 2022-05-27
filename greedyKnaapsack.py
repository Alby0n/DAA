def greedyKnapsack(items, capacity):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    knapsack = []
    current_capacity = capacity
    profit = 0
    # Loop through items
    for item in items:
        if item[1] <= current_capacity:
            knapsack.append(item)
            current_capacity -= item[1]
            profit += item[0]
    return profit

items = [(15, 3), (20, 2), (30, 10),(14,2)]
capacity = 6
print(greedyKnapsack(items, capacity)) 