import time
from sys import exit

y = int(input("minutes: "))
x = int(input("seconds: "))

if x > 60:
    y += int(x/60)
    x -= 60 * int(x/60)

if y or x > 0:
    while True:
        if y or x > 0:
            print(y, ":", x)
            x -= 1
            if x < 0:
                x += 60
                y -= 1
            time.sleep(1)
        else:
            print("done")
            exit()
else:
    print("done")
    exit()
