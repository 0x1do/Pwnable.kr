"Mommy! What is a file descriptor in Linux?
ssh fd@pwnable.kr -p2222 (PW: guest)"

Before entering the challenge, I searched "file descriptors in Linux",
and found this awesome YouTube video:

https://youtu.be/zMKacHGuIHI?si=U8X4kyTOPjtZ0xn7

If you only want to finish the CTF ASAP you just need the following picture:

int value | Name | file stream 
--- | --- | --- 
0 | Standard input | stdin 
1 | Standard output | stdout
2 | Standard error | stderr

Now, after that, we got a bit of background on the challenge, let's begin!
After I connected to the machine I saw 3 files: fd, fd.c, flag.
We have access to read fd.c and run fd (compiled fd.c), our mission is to get the content of the flag.
Let's try and run fd:
```bash
fd@pwnable:~$ ./fd
pass argv[1] a number
```

Okay, that's interesting. Let's try just any number (in order to pass argv[1] a number):
```bash
fd@pwnable:~$ ./fd 0
learn about Linux file IO
```
So it seems like it's not that simple, let's print fd.c and try to analyze it a bit:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];


int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");

                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;  
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;
})
```

After a quick glance at the code, I searched about atoi function and found [this](https://www.tutorialspoint.com/c_standard_library/c_function_atoi.htm). So atoi basically parse a string to int.
In order to succeed in the challenge we need to get to line 18 of the code, meaning we need the "LETMEWIN\n" == buf. 
From lines 13-14, we realize that we need to set fd to zero. 
To sum up, if fd equals zero we finished. I saw that fd = (the number we are giving) - 0x1234
I opened calc and converted 11234 in hex to decimal and got 4660.
After I wrote that we entered a shell and we need to write LETMEWIN in order to get the flag.
```bash
fd@pwnable:~$ ./fd 4660
LETMEWIN
good job :)
*the flag*
```
