# Little School Bus - 75
Problem:
```
Can you help me find the data in this file
littleschoolbus.bmp?
```
Hint:
```
Look at least significant bit encoding!!
```
This is the file: [littleschoolbus.bmp](kapifiles/littleschoolbus.bmp)
for LSB decoding I use [zsteg](https://github.com/zed-0xff/zsteg)
```
root@BOEING:# zsteg littleschoolbus.bmp 
imagedata           .. text: "~vtsoljmkhhfgXWWNNNVUV~}"
b1,lsb,bY           .. text: "flag{remember_kids_protect_your_headers_c1a3}"
b3,r,lsb,xY         .. file: very old 16-bit-int big-endian archive
b4,rgb,msb,xY       .. file: MPEG ADTS, layer I, v2, 112 kbps, 24 kHz, JntStereo
```

The flag was:
* flag{remember_kids_protect_your_headers_c1a3}
