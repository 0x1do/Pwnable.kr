Mommy! what is a file descriptor in Linux?
ssh fd@pwnable.kr -p2222 (pw:guest)

Before entering the challenge, I searched about file descriptors in linux,
and found this amazing youtube video: https://youtu.be/zMKacHGuIHI?si=U8X4kyTOPjtZ0xn7
If you only want to finish the ctf asap you just need the following picture:
![image](https://github.com/ido5ch/Pwnable.kr/assets/97401114/119d12e0-a921-47e9-adaf-148b5f5aa877)

Now, after that we got a bit of backgrounfd on the challenge, lets begin!
After I connected to the machine I saw 3 files: fd, fd.c, flag.
We have access to read fd.c and run fd (compiled fd.c), our mission is to get the content of flag.
Lets try and analyze fd.c (the whole code :
