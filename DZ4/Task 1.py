def twoCitySchedCost(costs):
    d_a = []
    d_b = []
    min_sum = 0
    for i in costs:
        min_sum += min(i)
        if i[0] > i[1]:
            d_b.append(i[0] - i[1])
        else:
            d_a.append(i[1] - i[0])
        
    d_a.sort()
    d_b.sort()
       
    if len(d_a) > len(d_b):
        difference_len = (len(d_a) - len(d_b)) // 2
        for i in range(difference_len):
            min_sum += d_a[0]
            d_a.pop(0)
        
    elif len(d_a) < len(d_b):
        difference_len = (len(d_b) - len(d_a)) // 2
        for i in range(difference_len):
            min_sum += d_b[0]
            d_b.pop(0)
       
    return min_sum

"""Сложность O(n)"""