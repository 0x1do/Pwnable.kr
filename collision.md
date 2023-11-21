"Daddy told me about cool MD5 hash collision today.
I wanna do something like that too!

ssh col@pwnable.kr -p2222 (pw: guest)"

What is a hash collision?
[for general knowledge](https://www.digitalwhisper.co.il/files/Zines/0x0C/DW12-1-HashCollisions.pdf), and for 
[a bit background](https://en.wikipedia.org/wiki/MD5#Collision_vulnerabilities)

Hash collision is when two different inputs get the same hash, and from there we can exploit it. How does it work? well, there are infinite inputs possible, and a limited amounts of outputs.

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
Interesting... Now let's try and enter a passcode 20 bytes long to see what will I get:
```bash
col@pwnable:~$ ./col `python -c 'print "a" * 20'`
wrong passcode.
```
It looks like I'm kind of stuck. Let's take a look at the source code:
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
Let's figure out what the code does. It saves a hex value named ```hashcode```, and there is the ```check_password``` function that gets our input, does some kind of simple hashing, and returns the "hash". In ```main``` it makes sure that our input is 20 bytes long and then compares ```hashcode``` to ```check_password(our input)```

Let's dive deeper into ```check_password```. The function takes the pointer to our input and converts it to an int pointer. Afterward, there is a for loop for 5 iterations that sum 5 ints and save the result on ```res```. Because it is a 4 byte, they will be all combined 20 bytes.

All we need to do is to write a script that enters 5 strings whose sum is equal to ```hashcode```.
So: 0x21DD09EC / 5.0 = 0x6C5CEC8 + 0.8.
0x21DD09EC - 4 * 0x6C5CEC8 = 0x6C5CECC
All we have left is to write our script and run:
```bash
col@pwnable:~$ ./col `python -c 'print "\xc8\xce\xc5\x06" * 4 + "\xcc\xce\xc5\x06"'`
*the flag*
```
