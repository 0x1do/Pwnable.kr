Mommy! What is a file descriptor in Linux?
ssh fd@pwnable.kr -p2222 (pw: guest)

Before entering the challenge, I searched file descriptors in Linux,
and found this amazing YouTube video:
https://youtu.be/zMKacHGuIHI?si=U8X4kyTOPjtZ0xn7

If you only want to finish the CTF ASAP you just need the following picture:
![image](https://github.com/ido5ch/Pwnable.kr/assets/97401114/119d12e0-a921-47e9-adaf-148b5f5aa877)

Now, after that, we got a bit of background on the challenge, let's begin!
After I connected to the machine I saw 3 files: fd, fd.c, flag.
We have access to read fd.c and run fd (compiled fd.c), our mission is to get the content of the flag.
Let's try and analyze fd.c :
