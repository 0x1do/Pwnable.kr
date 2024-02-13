└──╼ $./flag
I will malloc() and strcpy the flag there. take it.

└──╼ $upx -d flag
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    883745 <-    335288   37.94%   linux/amd64   flag

Unpacked 1 file.

└──╼ $ strings flag | grep ':)'
UPX...? sounds like a delivery service :)

note: I used grep :) because I noticed that all the flags contained it.
