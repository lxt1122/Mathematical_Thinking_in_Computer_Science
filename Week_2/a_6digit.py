# there is a 6-digit number starting by 100 and divisible by 9127 ?


for i in range(100000, 100999):
    if i % 9127 == 0:
        print(i)
