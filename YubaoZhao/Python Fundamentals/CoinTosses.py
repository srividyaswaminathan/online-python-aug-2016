#Assignment: Coin Tosses
#You're going to create a program that simulates tossing a coin 5,000 times.
#Your program should display how many times the head/tail appears.

def coin_tosses():
    head = 0
    tail = 0
    coin = ["head","tail"]
    import random
    for i in range(5000):
        num = round(random.random())
        if num == 1:
            head += 1
            idx = 0
        else:
            tail += 1
            idx = 1
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(i+1,coin[idx],head,tail)
    print "Ending the program, thank you!"

coin_tosses()
