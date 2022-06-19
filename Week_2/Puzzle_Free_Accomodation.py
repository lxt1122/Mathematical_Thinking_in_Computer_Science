# Question 1
# A town has three hotels. You have 10 vouchers for one-night stay for the first hotel, 15 for the second one,
# and 20 for the third one. The rules do not allow you to use vouchers for two consecutive nights in one hotel. Can
# you use them all for 10 + 15 + 20 = 45 consecutive nights changing the hotels each night?


# Question 1
#
# Find a 5-digit integer NNN such that N^2  starts with 27182.
import math

m: int

for m in range(10000,99999):
    if int(math.pow(m,2)/10000) == 27182:
        print("m =",m )


# Question 3
# There are some books on the table. If you group them by 3, you get some number of full groups and 2 books remain;
# if you group them by 4, you get some number of full groups and 3 books remain; if you group them by 5, you get some
# number of full groups and 4 books remain. What is the number of books on the table, if it is less than 100?


B: int

for B in  range(100):
    if B % 3 == 2 and B % 4 == 3 and B % 5 == 4:
        print("B=",B)




# Question4 # In some country there are 12-, 20-, and 30-florin coins only. One person in this country wants to pay
# some amount to other person in this country. What is the minimal amount that can be paid if both people have many
# coins of each type?


x:int
y:int
z:int

for x in range(-20,20):
    for y in range(-20,20)
        for z in range(-20,20)

