# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 2-August-2016
# Assignment: Coin Tosses
# You're going to create a program that simulates tossing a coin 5,000 times.
# Your program should display how many times the head/tail appears.

import random

def toss_coin():
    return round(random.random())

def sim_coin_tossing(n=5000):
    h = 0
    t = 0
    for i in range (n):
        print 'Attempt #' + str(i+1) + ': Throwing a coin... ',
        if toss_coin() == 1:
            h+=1
            print "It's a head! ... ",
        else:
            t+=1
            print "It's a Tail! ... ",
        print 'Got', h, 'head(s) so far and', t, 'tail(s) so far'

    print 'Ending the program, thank you!'
        

sim_coin_tossing()



