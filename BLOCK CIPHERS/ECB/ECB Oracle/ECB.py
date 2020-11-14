#!/usr/bin/env python3
from pwn import *
from string import printable

BLOCK = 32

def check(msg):
    p.recvuntil("encrypt:")
    p.sendline(msg)
    p.recvuntil("password: ")
    encrypted = p.recvline().decode('utf-8').strip()
    return encrypted

def block(str):
  return [str[i:i+BLOCK] for i in range(0, len(str), BLOCK)]

#counter = 11
counter = 31
test = ''
LETTERS =  string.printable[:-6]
#flag = "CCIT{r3m3mb3r_th3_3c"
flag = ''

p = remote('149.202.200.158', 7000)

for i in range(0,40):
    for c in LETTERS:
        print(c)
        test = flag
        test += c
        sendline = "A" * counter + test + "A" * counter
        print(sendline)
        result = block(check(sendline))
        print(result)
        if result[1] == result[3]:
            flag += c
            test += c
            counter -= 1
            #print(result)
        print("FLAG: {}".format(flag))

    # for r in result:
    #     print(r)

p.interactive()