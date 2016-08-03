import random

def toss_coins():
    info = {
        'head': 0,
        'tail': 0
    }
    for throw_num in range(0,5001):
        # Return a random element from the non-empty sequence
        rand_val = random.choice(['head','tail'])
        # Increment times
        info[rand_val] += 1
        # Print string
        print "Attempt #{}: Throwing a coin... It's a {}! ...Got {} head(s) so far and {} tail(s) so far.".format(throw_num, rand_val, info['head'], info['tail'])

toss_coins()
