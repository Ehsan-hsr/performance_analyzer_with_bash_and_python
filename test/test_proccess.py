from time import sleep 

def fibbonachi_series(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return (fibbonachi_series(num - 1) + fibbonachi_series(num - 2))

i = 1
while True:
    i += 1
    print(fibbonachi_series(i))
    sleep(.2)
