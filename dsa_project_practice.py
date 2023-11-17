dist = [1, 10, 20, 30]
speed = [10, 1, 1, 1]
time = []
for i, j in zip(dist, speed):
        res = round(i/j)
        time.append(res)
print(time)

def eliminate_maximum(dist, speed):
    min_reach = []
    for d, s in zip(dist, speed):
        minute = round(d / s)
        min_reach.append(minute)

    min_reach.sort()
    res = 0
    for minute in range(len(min_reach)):
        if minute >= min_reach[minute]:
            return res
        res += 1
    return res                                                          

# result = eliminate_maximum([3, 2, 4], [5, 3, 2])
# print(result)


# def eliminateMaximum(dist, speed):
#     n = len(dist)
#     arrival_time = [0] * n

#     for i in range(n):
#         arrival_time[i] = (dist[i] - 1) // speed[i]

#     arrival_time.sort()
#     for i in range(n):
#         if i > arrival_time[i]:
#             return i

#     return n

# result = eliminateMaximum([3, 2, 4], [5, 3, 2])
# print(result)


def eliminate_maximum(dist, speed):
    n = len(dist)
    min_reach = [0]*n
    for i in range(n):
        min_reach[i] = (dist[i]-1) // speed[i]

    min_reach.sort()
    r=0
    for minute in range(len(min_reach)):
        if minute >= min_reach[minute]:
            return res
        res += 1
    return res                                                          

result = eliminate_maximum([3, 2, 4], [5, 3, 2])
print(result)
