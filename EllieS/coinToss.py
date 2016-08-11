# Create a program that simulates throwing a coin 5,000 times.
# Your program should display how many times the head/tails appears

import random
for num in range(1,5001):
    possibilities =["heads", "tails"]
    coin = random.choice(possibilities)
    num += 0
    print "Attempt #{}. Throwing a coin. Its a {} ".format(num, coin) + " Got{} so far and {} so far".format(num, coin)
