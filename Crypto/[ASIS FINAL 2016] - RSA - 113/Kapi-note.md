# RSA - 113
```
Attachment: rsa.txz
```
```
[+] extract rsa.txz
rsa.txz:
	- flag.enc
	- pubkey.pem
	- rsa.py
```

### Check for public key: public.key
```
$ openssl rsa -in pubkey.pem -pubin -text -modulus
Public-Key: (256 bit)
Modulus:
    00:d8:e2:4c:12:b7:b9:9e:fe:0a:9b:c0:4a:6a:3d:
    f5:8a:2a:94:42:69:b4:92:b7:37:6d:f1:29:02:3f:
    20:61:b9
Exponent:
    00:ac:2a:c3:e0:ca:0f:56:07
Modulus=D8E24C12B7B99EFE0A9BC04A6A3DF58A2A944269B492B7376DF129023F2061B9
writing RSA key
-----BEGIN PUBLIC KEY-----
MEIwDQYJKoZIhvcNAQEBBQADMQAwLgIhANjiTBK3uZ7+CpvASmo99YoqlEJptJK3
N23xKQI/IGG5AgkArCrD4MoPVgc=
-----END PUBLIC KEY-----
```

### Use [yafu](https://sourceforge.net/projects/yafu/) to factor it if it's possible.
```
yafu-x64.exe factor(0xd8e24c12b7b99efe0a9bc04a6a3df58a2a944269b492b7376df129023f2061b9)
***factors found***

P39 = 311155972145869391293781528370734636009
P39 = 315274063651866931016337573625089033553
```
Then we found that there are only 2 prime numbers, then this RSA key is weak for factoring attack.



### Use rsatool.py to generate private key from these 2 prime numbers.
```
$ rsatool.py -p 311155972145869391293781528370734636009 -q 315274063651866931016337573625089033553 -o priv.key
Using (p, q) to initialise RSA instance

n = d8e24c12b7b99efe0a9bc04a6a3df58a2a944269b492b7376df129023f2061b9

e = 65537 (0x10001)

d = 880daddb3015e97f43f860b04de580597ca8dd7821532e9667dbbe37ba954c01

p = 311155972145869391293781528370734636009 (0xea1675dda1710f66b01006cb205b1be9)

q = 315274063651866931016337573625089033553 (0xed2f9373ec01867aabbbbc05d9190551)

Saving PEM as priv.key
```

### Read flag.txt
```
$ cat flag.enc 
mBvIRwW8Q7hkNINbXmTGxscnVjfZ9nVG2AaOYHeTRYsRezHMkpFW15q3NqENPLJGyLlDALb5Cycd
TV9ok/NXoUnnXx3MQLQnBVax2pmZ3bkUBbaRIWyVB2UHcZKpH8UFPT2uFnDSnhOG8PBJ9RCCs2ew
UoJ1wBxV8W7qBmMe6TmoEn6g0/sOte5o7lp5oJMCbWObhjNpxHtrREryTdulDgRVlWbvbpV/m4V1
V7U1a2FQuAQpEMcIMAgWXllzsfGCOPI1iHh7IodWkNjc1sIMOzeqf05L0f393h14GR1/JqPAZJTs
QjM/aB4QkZuH7rPHqyaM5mNsZ1+KPRZsLfYRcTBaiM/mBg/aNWWZg9kvzovP+Zs5EPkJepAYTmLs
l4t5mjkMdJ64nvXJiOcNwHVfClQjyVwJcdeguu1CAsU81CZnYo+Yixh129gCQuMkgQN3t9Pb+zz8
Edl2HlpOwcfT99C/EcQVfNmsHn96Y3LPUkFVPUquhNaMDmsYVbRyxeoa2Rktwr4Ia4Rhi1HQb7jz
Ehql8R4H9HS/wrPueqc5nL2odfC7ctThes6sA447oBCnkb95NVQLRiJlhYJvan2Vy/wySJJArrX4
PiY5Qh+dMrZnHP9XMFs5CFu6PIH9Iy5pwi9SQenUZJ3ajm8fDc6Vtpi+dRNEh78hlZ8iZu0p403i
UE8PEwp6qYf2StIjq/JU+LAEqhR9cn6parxDhZt3ftfq0SIbGSPZ42832Yyhr6GKwYBguHJIvXHi
bo3zIgxPiTLwxseaY9N4KrPWyNpL9Uq14qQt7cNLWfhv/e3vlIReZjWgqBYZYS90FjJt04VPWmUU
i4O8RCgCqPfd1Oc3OS9UB7NnvcN4SQQ5CowA3AJxrd/8vjTBgV0CS5ZxV48yapB9iHOvR7PGJVY4
79q7eQDqf3lSOeQ7DH0Y/wA+HJMw1HGP1BfWD0Fu7PsWxHmBEPkusIc8gxg+y7N1/d2YaWcpe0N0
cXUd1Jm02W+5b1vOfpwbOcGh4eZTS2SN4Iu/uDKWwThD0C9po35qZTC67QUeYU+7u9EafVD+ETQz
9DHo8kP9jYKnjpsP3mPlv7nj1sHEMA52tfNclxagj8haf101V3lH453UBhzQjFOlo7XGFD/fH+HU
Xhszsj6oPttU99qBoun0HSQtK+JhEIjTTj/kO8/rT+jqfSiSf24Ermvxf6ooqYG/HKXShWEkYHBp
yA9cAu5/k1EgKKrkj1SlOcGPfNYiaCvCwok5IZR6cMjYy5H9UXn+naedLSk1r6iG5lY52zXCBm9i
akgyEobAUxUPhENrrM2x/pBNUL5Kpi/z5IrjHiVotCqbofkZK3YX0PjOpaQVwtoklaA5uHvGk5mT
UIVlXPJKice9G6sPu16Ugi0xfaRm2iDAMK5feq527mCI5+pkA8ATjJinh+UxfN50YYN7zzgBBOVh
Kj2MH0mnsHXeYipRM5lFDmTGNCSF/NVu2yo3cayxWFmnWU6kU+TWGgFKN4xdFm/dzb3oO23rhEkP
QKHMdkDweGFzqxXcv7qJICGG/xXKDkcCdVWaRWsNXLHh21Z3cjf0hWsx8bjufB352uDCYGm+oYtM
PdN2SZTdPy937IbVjO9v56+1zpt5zvNc2xyj/jOfr5DVklh/c9h3Cvnx45gukabAsFbhXy8lUU84
uyQmO12MhPK4jSvXQglEsJVqk3UYGiYSkPeWPplMWYzLXurJM0OBsfB9gfFt30C2fdQvgh4b2TWe
O8PZnsf4oaQT9v16A5Z1bniVbb5UVqsn234g3BPOSUGVaEvglANBt07+vNTa6fQ+QhrR/j19csU0
xxgplIzswzf8gue6CWBsaqUV7Sqq7mpPEYOucJ0RMqZCyaA4ACTqpZn8hedIiQWBa02519QyYbwE
AKSwS2/zXINK7wlC/acryghivN3ciKK8Aio7XXuYZ+92NC1sCFsFutySJMcRx09qbQDxu4r/22Wc
4VsH9S/lM0SvIfP0mBQt1Kk2qNJoTX+6Vsa2OFHgwNOubwZga+WBF7gP4zCxI2JQvgoHXdxjikeX
czlDYlQ5KBcK4E3QZKIj7yVH5R1g5noMoEwsj7AYKKJ2pbx9yadMEev9O+7JHg/GIsA+56WcZRC6
UqtFWqBOJVr7WEIk5HI0yyB5oZHKmAf3iWG8r94J84TTKxnbpqSV/t5GT6JZJegaIx2CuwYhTXCM
a3lBtQfDMfdZ/ZvrlnK/+hhE420/x1Z8qHDRfc+ZTbCDOh+RIwlZ32aXvRfEdzTU5YdRBdfAeuXz
GbfDDRmwOLNFX2vC80MXFBpAFYDhHtYsuEx3IWY0mwaftMjgCLjnoMA2D6culnbJ3O3cwsqksqgV
9Axv5GdqqPMANj1FsJo5A97wuOjA7pRG2kMwEIijfx/cPZnIha/rTX3iYuI441qx9bi+l6rw0HvF
qlM+r18eoTOGdN4egNiho5YeMaVzm+bgkVBRYMtxl150ntfdBx7wgFL/8AnPmNH3PA1hhwHaW/0v
LWRXc0M/uB3MD0TG61mlWIDOCJYAn4BasWjYgluMT0Gl31kfM0TiENuY547ZRvAikXWDjbt2wNAA
Dvn/4QIOv/vAI7k4o1m98R94+IQUvTkdOxs5J+R7m6hW7F1FWXKnJcRFV9VyN7VtnFBGfdJihFu1
y4lIBQb5cmZXgaDWsQdrQr2JaAj481Qon227LvpkKWiMz60y5Mv2JCpFZHhtEnQUIsFzX92bGpSC
BXpj6EueRnTnUL695Dq1I6VfjCYnrxMYeuvUCFFJGrX1087TSrFk60yWvYpndx5kUA0/2jCbLFzq
aNfYEE7CT9si10BQqOaeWQ6OJGTg0kGwmykXN/pBZmzxG/EkgK94l66o+W9aScXV5XZfQfz7Tfw0
AknUqW4U
```
### Let's decrypt it!!! 
Decrypt it using python script
```
import sys
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5

def decrypt_RSA(privkey,cipherfile):
    key = open(privkey, "r").read()
    cipher = open(cipherfile, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_v1_5.new(rsakey)
    decrypted = rsakey.decrypt(base64.b64decode(cipher), None)
    return decrypted
 
 
print decrypt_RSA("priv.key", "flag.enc")
```
```
$ python decrypt.py
Traceback (most recent call last):
  File "decrypt.py", line 15, in <module>
    print decrypt_RSA("priv.key", "flag.enc")
  File "decrypt.py", line 11, in decrypt_RSA
    decrypted = rsakey.decrypt(base64.b64decode(cipher), None)
  File "/usr/lib/python2.7/dist-packages/Crypto/Cipher/PKCS1_v1_5.py", line 204, in decrypt
    raise ValueError("Ciphertext with incorrect length.")
ValueError: Ciphertext with incorrect length.
```
I've tried to use openssl and my python script to decrypt it but it become fail with an error
"ValueError: Ciphertext with incorrect length."

Let's check for the last file they gave us.
```
$ cat rsa.py
#!/usr/bin/python

import gmpy
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

flag = open('flag', 'r').read() * 30

def ext_rsa_encrypt(p, q, e, msg):
    m = bytes_to_long(msg)
    while True:
        n = p * q
        try:
            phi = (p - 1)*(q - 1)
            d = gmpy.invert(e, phi)
            pubkey = RSA.construct((long(n), long(e)))
            key = PKCS1_v1_5.new(pubkey)
            enc = key.encrypt(msg).encode('base64')
            return enc
        except:
            p = gmpy.next_prime(p**2 + q**2)
            q = gmpy.next_prime(2*p*q)
            e = gmpy.next_prime(e**2)

p = getPrime(128)
q = getPrime(128)
n = p*q
e = getPrime(64)
pubkey = RSA.construct((long(n), long(e)))
f = open('pubkey.pem', 'w')
f.write(pubkey.exportKey())
g = open('flag.enc', 'w')
g.write(ext_rsa_encrypt(p, q, e, flag))
```
There are things we've noticed:
* flag = open('flag', 'r').read() * 30 - flag has been multiple by 30 times so flag will be very big. This will cause an error because of length of the message.
* try: ... exection: ... - pubkey.pem was generated from originated p, q value but when an error has occured p, q, e, and n will be changed. We need to calculate p, q, e, and n in the same way the encryption method did.

```
import gmpy
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

def decrypt_RSA(cipherfile):
    n = 98099407767975360290660227117126057014537157468191654426411230468489043009977
    e = 12405943493775545863
    p = 311155972145869391293781528370734636009
    q = 315274063651866931016337573625089033553
    cipher = open(cipherfile, "r").read()
    while True:
        try:
            # key = open(privkey, "r").read()
            phi = (p - 1)*(q - 1)
            d = gmpy.invert(e, phi)
            # pubkey = RSA.construct((long(n), long(e)))

            privkey = RSA.construct((long(n), long(e), long(d)))
            key = PKCS1_v1_5.new(privkey)
            decrypted = key.decrypt(base64.b64decode(cipher), None)
            print decrypted
            break
        except Exception as ex:
            print ex
            p = gmpy.next_prime(p**2 + q**2)
            q = gmpy.next_prime(2*p*q)
            e = gmpy.next_prime(e**2)
            n = long(p)*long(q)

decrypt_RSA("flag.enc")
```
Then we've got flag.
* ASIS{F4ct0R__N_by_it3rat!ng!}
