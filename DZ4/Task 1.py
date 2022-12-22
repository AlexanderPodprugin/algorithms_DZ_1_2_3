# def twoCitySchedCost(cost):
#     cost.sort(key=lambda x: x[0] - x[1])
#     n = len(cost) // 2
#     res = 0
#     for i in range(len(cost)):
#         n -= 1
#         if n < 0:
#             res += cost[i][1]
#         else:
#             res += cost[i][0]
#     return res

def twoCitySchedCost(cost):
        dif_a = [] #
        dif_b = []
        min_sum = 0
        for i in cost:
            min_sum += min(i)
            if i[0] > i[1]:
                dif_b.append(i[0] - i[1])
            else:
                dif_a.append(i[1] - i[0])
        
        dif_a.sort()
        dif_b.sort()
       
        if len(dif_a) > len(dif_b):
            difference_len = (len(dif_a) - len(dif_b)) // 2
            for i in range(difference_len):
                min_sum += dif_a[0]
                dif_a.pop(0)
        
        elif len(dif_a) < len(dif_b):
            difference_len = (len(dif_b) - len(dif_a)) // 2
            for i in range(difference_len):
                min_sum += dif_b[0]
                dif_b.pop(0)
       
        return min_sum

print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))