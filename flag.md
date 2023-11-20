"Papa brought me a packed present! let's open it.

Download: http://pwnable.kr/bin/flag

This is reversing task. all you need is binary"

Let's run it:
```bash
└──╼ $./flag
I will malloc() and strcpy the flag there. take it.
```
Let's understand what is [Malloc](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/) and how does it work.
Now that we have all the information that we can get, let's open ida and disassemble the file.
Damn, we have just so many functions. I am not going to understand all, let's try and think what to do.

![giphy](https://github.com/ido5ch/Pwnable.kr/assets/97401114/707ab752-1857-449c-9971-4b1c2fdf996e)

Strings! We already understand that the challenge is about locating a string, so let's press view strings (view -> Open subviews -> strings):
'12Wr%W345%Wr%67x!Wr892    //upx.sf.net $\n    proc/self/exe
The first and last strings don't seem as interesting as the second one, which looks like a domain.
I entered the domain and installed upx. Let's reopen the terminal and try to use that.
```bash
└──╼ $upx
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

Usage: upx [-123456789dlthVL] [-qvfk] [-o file] file..

Commands:
  -1     compress faster                   -9    compress better
  -d     decompress                        -l    list compressed file
  -t     test compressed file              -V    display version number
  -h     give more help                    -L    display software license
Options:
  -q     be quiet                          -v    be verbose
  -oFILE write output to 'FILE'
  -f     force compression of suspicious files
  -k     keep backup files
file..   executables to (de)compress

Type 'upx --help' for more detailed help.

UPX comes with ABSOLUTELY NO WARRANTY; for details visit https://upx.github.io
```
It looks like we only need to decompress the file, so let's do it:
```bash
└──╼ $upx -d flag
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    883745 <-    335288   37.94%   linux/amd64   flag

Unpacked 1 file.
```
Let's take and disassemble the new file. We'll take a look at the strings and the flag is right there!
