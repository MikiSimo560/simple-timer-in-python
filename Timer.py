import time
y = int(input("minutes: "))
x = int(input("seconds: "))
if x > 60:
    y += int(x/60)
    x -= 60
if y or x > 0:
    while True:
        print(y, ":", x)
        x -= 1
        if x < 0:
            x += 60
            y -= 1
        time.sleep(1)
else:
    print("done")
