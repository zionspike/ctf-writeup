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