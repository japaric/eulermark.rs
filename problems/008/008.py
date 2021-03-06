WINDOW = 13


def product(digits):
    p = 1

    for digit in digits:
        p *= digit

    return p


def f():
    digits = [0] * WINDOW
    max_, pos = 0, 0

    with open("008.txt") as f:
        for char in f.read():
            if char != '\n':
                digits[pos] = int(char)

                p = product(digits)

                if p > max_:
                    max_ = p

                pos = (pos + 1) % WINDOW

    return max_

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


if len(sys.argv) == 1:
    print(f())
elif len(sys.argv) == 2:
    start, end = timespec(), timespec()
    iters = int(sys.argv[1])

    clock_gettime(CLOCK_MONOTONIC, ctypes.pointer(start))
    for _ in range(0, iters):
        f()
    clock_gettime(CLOCK_MONOTONIC, ctypes.pointer(end))

    print(to_ns(end) - to_ns(start))
