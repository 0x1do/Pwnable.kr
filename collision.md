"Daddy told me about cool MD5 hash collision today.
I wanna do something like that too!

ssh col@pwnable.kr -p2222 (pw: guest)"

What is a hash collision?
[for general knowledge](https://www.digitalwhisper.co.il/files/Zines/0x0C/DW12-1-HashCollisions.pdf), and for 
[a bit background](https://en.wikipedia.org/wiki/MD5#Collision_vulnerabilities)

Now, that we understand that, let's continue to the challenge.
As before we have col.c col flag (code in c, the compiled code, flag.
Let's try and run col:
```bash
col@pwnable:~$ ./col
usage : ./col [passcode]
```
Oh. Seems like we need to enter a passcode, let's try something:
```bash
col@pwnable:~$ ./col idontknow
passcode length should be 20 bytes
```
Interesting... Now I'm going to enter an input 20 bytes long:
```bash
col@pwnable:~$ ./col `python -c 'print "a" * 20'`
wrong passcode.
```
Let's take a look at the source code:
```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```
So the code does some kind of a simple hashing to the input and then compares it to the hashcode that they already configured (0x21DD09EC).
If you know how to count up to 20, you'll see that if we put the hash it won't work because it's less than 20 digits. 
![giphy](https://github.com/ido5ch/Pwnable.kr/assets/97401114/979c7be6-ac3f-40cc-9beb-82f0195b435d)

After a bit of looking and logically reversing the check_password function. It looks like we just need to give them 5 numbers and their sum is the hash.
So: 0x21DD09EC / 5.0 = 0x6C5CEC8 + 0.8.
0x21DD09EC - 4 * 0x6C5CEC8 = 0x6C5CECC
All we have left is to write our script and run:
```bash
col@pwnable:~$ ./col `python -c 'print "\xc8\xce\xc5\x06" * 4 + "\xcc\xce\xc5\x06"'`
*the flag*
```
