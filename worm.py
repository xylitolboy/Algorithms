#A worm is at the bottom of a pole. It wants to reach the top, but it is too lazy to climb to the top without stopping. 
#It can crawl up the pole a certain number of inches at a time, falling down a lesser number of inches right after while it rests. 
#How many times does the worm need to crawl up in order to reach the top of the pole?

#The input consists of a single line that contains three integers $a, b$ ($0 \leq b < a \leq 100$),
#and $h$, ($0 < h \leq 100\,000$) indicating the amount $a$ of inches the worm can climb at a time, the amount $b$ of inches the worm falls during its resting period, and the height $h$ of the pole, respectively.
#Note: For the purposes of this problem, the worm is modeled as a point and thus has no length.

a,b,c = (map(int,input().split()))
sum = 0
cnt = 0

while True:
    sum += a
    cnt += 1
    if (sum >= c):
        break
    else:
        sum -= b

print (cnt)

