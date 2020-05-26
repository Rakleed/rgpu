import math

r = 0.0373
time = 0
n = 26
t = 83
ts = 22


def func(t, ts, time):
    return ts - (ts-t) * math.exp(-r*time)


for time in range(0, n):
    print("time = {}, T = {:.4f}".format(time, func(t, ts, time)))
