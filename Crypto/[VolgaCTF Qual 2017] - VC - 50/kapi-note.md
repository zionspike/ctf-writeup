# VC - 50
Problem:
```
There are files A.png and B.png. But where's the flag?
A.png
B.png
```
For file A.png and B.png I've checked for file type and [Exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool/) but there are nothing suspicious. 

```
root@AIRBUS:# exiftool A.png 
ExifTool Version Number         : 10.47
File Name                       : A.png
Directory                       : .
File Size                       : 17 kB
File Modification Date/Time     : 2017:03:24 16:19:58-04:00
File Access Date/Time           : 2017:03:26 09:06:54-04:00
File Inode Change Date/Time     : 2017:03:25 08:55:06-04:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 370
Image Height                    : 370
Bit Depth                       : 1
Color Type                      : Grayscale
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 370x370
Megapixels                      : 0.137
root@AIRBUS:# exiftool B.png 
ExifTool Version Number         : 10.47
File Name                       : B.png
Directory                       : .
File Size                       : 17 kB
File Modification Date/Time     : 2017:03:24 16:20:02-04:00
File Access Date/Time           : 2017:03:26 11:33:38-04:00
File Inode Change Date/Time     : 2017:03:25 08:55:06-04:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 370
Image Height                    : 370
Bit Depth                       : 1
Color Type                      : Grayscale
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 370x370
Megapixels                      : 0.137
root@AIRBUS:# 
```
Both of them are Grayscale image that mean no color applied to the images. I check for color by reading the images and printing the pixel value of them using python code. 
```python
from PIL import Image
im = Image.open("solve.png","r")
pix_val = list(im.getdata())
for x in pix_val:
	print x
```

I found that there are only 2 values 0 and 255. I merge 2 images using python again.
```python
import Image

with open('pixA.txt') as f:
    linesA = f.read().splitlines()

with open('pixB.txt') as f:
    linesB = f.read().splitlines()

int_listA = [int(i) for i in linesA]
int_listB = [int(i) for i in linesB]
int_listC = []
for i in range(0,len(int_listA)):
	C = 255
	if int_listA[i] != int_listB[i]:
		C = 0
	int_listC.append(C)

# print int_list
im = Image.new('L', (370, 370))
im.putdata(int_listC)
im.save('solve.png')
```
Now I found the flag.
![flag](kapi-files/solve.png)

The flag was:
* VolgaCTF{Classic_secret_sharing_scheme}
