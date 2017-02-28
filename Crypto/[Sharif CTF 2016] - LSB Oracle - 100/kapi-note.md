
# lsb oracle - 100
```
Attachment: lsb-oracle-150.zip
```
```
[+] extract lsb-oracle-150.zip
crypto100.zip
	- description.py
	- lsb_oracle.vmp.exe
```
### Let's check for description.py
```
#! /usr/bin/env python3
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long
n = -1  # get it from the provided EXE file
e = -1  # get it from the provided EXE file
flag = b'' # redacted
key = RSA.construct((n, e))
cipher = PKCS1_v1_5.new(key)
ctxt = bytes_to_long(cipher.encrypt(flag))
print(ctxt)
# output is:
# 2201077887205099886799419505257984908140690335465327695978150425602737431754769971309809434546937184700758848191008699273369652758836177602723960420562062515168299835193154932988833308912059796574355781073624762083196012981428684386588839182461902362533633141657081892129830969230482783192049720588548332813
```
and then we check for lsb_oracle.vmp.exe
```
C:>lsb_oracle.vmp.exe
Usage:
        lsb_oracle.exe /? : Prints usage.
        lsb_oracle.exe /story : My story.
        lsb_oracle.exe /pubkey : Public key.
        lsb_oracle.exe /decrypt : Decryption mode.

C:>lsb_oracle.vmp.exe /story
 **********************************************************************************
 *  I used to be able to decrypt perfectly.                                       *
 *  But they did something terrible to me.                                        *
 *  I heard them saying:                                                          *
 *    We will make the life of any reverser miserable...                          *
 *    We will only allow a real cryptographer to get the pearl within this clam!  *
 *  They gagged my mouth, and restructured my body.                               *
 *  I can only utter one bit of the plaintext now.                                *
 **********************************************************************************

C:>lsb_oracle.vmp.exe /pubkey
n = 120357855677795403326899325832599223460081551820351966764960386843755808156627131345464795713923271678835256422889567749230248389850643801263972231981347496433824450373318688699355320061986161918732508402417281836789242987168090513784426195519707785324458125521673657185406738054328228404365636320530340758959
e = 65537

C:>lsb_oracle.vmp.exe /decrypt
Enter a valid ciphertext, and I'll return the LSB of its decryption. Enter -1 when you're done.
2201077887205099886799419505257984908140690335465327695978150425602737431754769971309809434546937184700758848191008699273369652758836177602723960420562062515168
299835193154932988833308912059796574355781073624762083196012981428684386588839182461902362533633141657081892129830969230482783192049720588548332813
1
Enter a valid ciphertext, and I'll return the LSB of its decryption. Enter -1 when you're done.

C:>
```
The last one number 1/0 is the least significant bit(LSB) So we now know we have to decrypt the cipher text given in description.py with 2 options:
* Reverse the binary and get private key
* Attack LSB oracle
Since reversing was protected by VMProptect it would take long time to do so. Then we will extract plaintext using LSB oracle. Let talk about it a little.

### LSB oracle
RSA left a single LSB bit of encryption as a parity. When we could determine the result of decrytion of RSA that remain even or odd number
then we could extract the hole plaintext. But there are things you should know in common of RSA:
* If a plaintext is even the result of decryption will return LSB of 0, and return LSB of 1 for odd plaintext.
* When we multiply two ciphers (encrypted with the same public key) the result is the same with multiplying 2 plaintexts and encrypt with the public key. Then if we multiply the cipher text with cipher of encrypted 2 it is the result of multiplying plain text with 2.
* For RSA:
	* encryption: c(cipher) = pow(m, e) mod n
	* decryption: m(plaintext) = pow(c, d) mod n
* When we decrypt multiplied by 2 cipher:
	* decryption: 2m = pow(new_c, d) mod n

### Take a more deep look at decryption of 2m.
1. if 2m is more than n then the result LSB would be 0 and we got m > n/2
2. if 2m is less than n then the result LSB would be 1 and we got m < n/2
.
.
.
x. if 2(2(2(2m))) is more than n then the result LSB would be 0 and we got m > n/2/2/2/2
y. if 2(2(2(2m))) is less than n then the result LSB would be 1 and we got m < n/2/2/2/2 (n is odd coz' n is the result of 2 primes p * q)
.
. and go on until the length of encryption key then we will get that possible m would be in scope of UPPER and LOWER boundary.

This is also known as Side-channel attack.

### Write an algorithm
```
_n = n
_e = e
_c = cipher
c_of_2 = pow(2, _e, _n)

lower = 0
upper = _n

tc = _c

for i in range(k):
    even = True
    process = call_process("lsb_oracle.vmp.exe /decrypt")
    output = input_to_process(tc)
    result = output.find_result_of_decryption_LSB()
    if result == 1:
        even == False
    possible_plaintext = (lower + upper)/2
    if even == True:
        upper = possible_plaintext
    else:
        lower = possible_plaintext
    tc = (tc*c_of_2)%_n

print "upper: " + str(upper) + " " + str(long_to_bytes(upper))
print "lower: " + str(lower) + " " + str(long_to_bytes(lower))
```

### Let write a code
```
#!/usr/bin/python
from subprocess import call
import libnum, decimal
import os
from subprocess import Popen, PIPE
from Crypto.Util.number import *

# obtained from /pubkey
_n = 120357855677795403326899325832599223460081551820351966764960386843755808156627131345464795713923271678835256422889567749230248389850643801263972231981347496433824450373318688699355320061986161918732508402417281836789242987168090513784426195519707785324458125521673657185406738054328228404365636320530340758959
_e = 65537

# obtained from description.py
_c = 2201077887205099886799419505257984908140690335465327695978150425602737431754769971309809434546937184700758848191008699273369652758836177602723960420562062515168299835193154932988833308912059796574355781073624762083196012981428684386588839182461902362533633141657081892129830969230482783192049720588548332813

k = _n.bit_length()
decimal.getcontext().prec = k

print "key bit length: " + str(k)
print "[+] Please wait..."

c_of_2 = pow(2, _e, _n)
tc = _c

tc_arr = []
print "First TC>" + str(tc)
for i in range(k):
    tc = (tc*c_of_2)%_n
    tc_arr.append(str(tc))   
tc_arr.append("-1")

# oracle
p = Popen(['wine','lsb_oracle.vmp.exe','/decrypt'], stdin=PIPE, stdout=PIPE)
out, err = p.communicate(os.linesep.join(tc_arr))
out_arr = out.split("Enter a valid ciphertext, and I'll return the LSB of its decryption. Enter -1 when you're done.")

# prepare result of oracle in form of array [1,0,0,............,0,1,1]
result_arr = []
for y in out_arr:
    if str(y).strip() == "1" or str(y).strip() == "0":
        result_arr.append(int(str(y).strip()))

# calculate plaintext from result of oracle
lower = decimal.Decimal(0)
upper = decimal.Decimal(_n)
print "len(result_arr):>" + str(len(result_arr))
print "oracle:>" + ''.join(str(result_arr))
for i in result_arr:
    possible_plaintext = (lower + upper)/2
    if i == 0:
        upper = possible_plaintext
    else:
        lower = possible_plaintext
    if str(long_to_bytes(upper)).find("Sherif") > 0 or str(long_to_bytes(lower)).find("Sherif") > 0:
        break

print "upper:>" + str(upper) + " " + str(long_to_bytes(upper))
print "lower:>" + str(lower) + " " + str(long_to_bytes(lower))
```
Waiting for a couple of minutes and get the flag.
* SharifCTF{65d7551577a6a613c99c2b4023039b0a}