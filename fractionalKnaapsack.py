def fractionalKnaapsack(items, capacity):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    totalValue = 0.0
    for item in items:
        if item[1] < capacity:
            totalValue += item[0]
            capacity -= item[1]
        else:
            totalValue += item[0] * capacity / item[1]
            capacity = 0
            break
    return totalValue

items = [(15, 3), (20, 2), (30, 10),(14,2)]
capacity = 6
print(fractionalKnaapsack(items, capacity)) 