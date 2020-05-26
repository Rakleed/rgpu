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


for k in range(n - 1, 0, -1):
    for row in range(k - 1, -1, -1):
        if m[row, k]:
            # 1) Make all overlying elements equal to zero in the former identity matrix
            m[row, :] -= m[k, :] * m[row, k]


return np.hsplit(m, n // 2)[1]
