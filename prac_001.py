lst = [[i * j for j in range(2, 10)] for i in range(2, 10)]

for i in range(9) :
    for j in range(9) :
        print(i, '*', j, '=', i * j)