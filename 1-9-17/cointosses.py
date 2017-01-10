import random
import math
heads = 0
tails = 0
for x in range(0,5):
    print "Starting the program..."
    num = random.random()
    print num
    num_rounded = round(num)
    print num_rounded
    if(num_rounded<0.50):
        heads = heads+1
        print "Attempt#",x,":","Throwing a coin... It's a head!...Got",heads,"head(s) so far and",tails,"tail(s) so far"
    else:
        tails = tails+1
        print "Attempt#",x,":","Throwing a coin... It's a tail!...Got",heads,"head(s) so far and",tails,"tail(s) so far"
print "Ending the program, thank you!"
