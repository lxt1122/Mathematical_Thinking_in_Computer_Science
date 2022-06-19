#  Question 1

#   Person A has an unlimited number of 7-florin coins, person B has an unlimited number of 13-florin coins. How A
# can pay 5 florins to B?


i: int
j: int

for i in range(-100,100):
    for j in range(-100,100):
        if 7* i + 13 * j == 5:
            print(i, j)
