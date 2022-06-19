# there is a 6-digit number starting by 100 and divisible by 9127 ?


for i in range(100000, 100999):
    if i % 9127 == 0:
        print(i)


for j in range(100, 999):

    if j % 2 == 1 and j % 3 == 1 and j % 4 == 1 and j % 5 == 1 and j % 6 == 1 and j % 7 == 1:
            print(j)