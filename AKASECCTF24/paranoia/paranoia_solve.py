#!/usr/bin/python3
from ctypes import CDLL
from pwn import *

libc = CDLL("libc.so.6")

p = remote("20.80.240.190", 1234)
# p = process("./paranoia")

libc.srand(libc.time(0))

flag = ""

for i in range(0x24):
    x = libc.rand()
    x = x % 0x100
    y = p.recvuntil(b" ")
    y = y[:-1]
    y = int(y.decode(), 10)
    flag += chr(x ^ y)

print(flag)