def step_sum(start, end, step):
    s, e = (start - 1) // step + 1, (end - 1) // step

    return step * (e * (e + 1) // 2 + s * (s + 1) // 2)


def f():
    s, e = int(0), int(1000)

    return step_sum(s, e, 3) + step_sum(s, e, 5) - step_sum(s, e, 15)

import ctypes
import sys

CLOCK_MONOTONIC = 1


class timespec(ctypes.Structure):
    _fields_ = [
        ('tv_sec', ctypes.c_long),
        ('tv_nsec', ctypes.c_long)
    ]

librt = ctypes.CDLL('librt.so.1')
clock_gettime = librt.clock_gettime
clock_gettime.argtypes = [ctypes.c_int, ctypes.POINTER(timespec)]


def to_ns(ts):
    return ts.tv_sec * int(1e9) + ts.tv_nsec


def ns_per_iter(start, end, iters):
    return (to_ns(end) - to_ns(start)) // iters

if len(sys.argv) == 1:
    print(f())
elif len(sys.argv) == 2:
    start, end = timespec(), timespec()
    iters = int(sys.argv[1])

    clock_gettime(CLOCK_MONOTONIC, ctypes.pointer(start))
    for _ in range(0, iters):
        f()
    clock_gettime(CLOCK_MONOTONIC, ctypes.pointer(end))

    print(ns_per_iter(start, end, iters))
