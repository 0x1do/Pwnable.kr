"Mommy! What is a file descriptor in Linux?
ssh fd@pwnable.kr -p2222 (PW: guest)"

Before entering the challenge, I searched "file descriptors in Linux",
and found this awesome YouTube video:

https://youtu.be/zMKacHGuIHI?si=U8X4kyTOPjtZ0xn7

If you only want to finish the CTF ASAP you just need the following picture:
![image](https://github.com/ido5ch/Pwnable.kr/assets/97401114/119d12e0-a921-47e9-adaf-148b5f5aa877)

Now, after that, we got a bit of background on the challenge, let's begin!
After I connected to the machine I saw 3 files: fd, fd.c, flag.
We have access to read fd.c and run fd (compiled fd.c), our mission is to get the content of the flag.
Let's try and run fd:
![image](https://github.com/ido5ch/Pwnable.kr/assets/97401114/6703dbf9-a2bb-4503-838e-2cfcb208d622)

Okay, that's interesting. Lets try just any number (in order to pass argv[1] a number):
![image](https://github.com/ido5ch/Pwnable.kr/assets/97401114/a0e99cad-557d-4f06-b04e-310060298045)

So it seems like its not that simple, let's print fd.c and try to analyze it a bit:
![image](https://github.com/ido5ch/Pwnable.kr/assets/97401114/657a852c-853f-4c6c-b451-d50185778860)

After a quick glance at the code I searched about atoi function, and found [this](https://www.tutorialspoint.com/c_standard_library/c_function_atoi.htm). So atoi basically parse string to int.
In order to succeed the chakknge we need to get to line 18 of the code, meaning we need the "LETMEWIN\n" == buf. 
From lines 13-14 we realize that we need to set fd to zero. 
To sum up, if fd equals to zero we finished. I saw that fd = (the number we are giving) - 0x1234
I opened calc and converted 11234 in hex to decimal and got 4660.
After I wrote that we entered a shell and we need to write LETMEWIN in order to get the flag.
![image](https://github.com/ido5ch/Pwnable.kr/assets/97401114/aba49b5e-ec42-434f-97ec-8330f7039628)



