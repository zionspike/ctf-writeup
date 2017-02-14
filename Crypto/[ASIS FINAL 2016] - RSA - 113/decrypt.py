import sys
import base64
import codecs
import gmpy
import math
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5

def decrypt_RSA(cipherfile):
	n = 98099407767975360290660227117126057014537157468191654426411230468489043009977
	e = 12405943493775545863
	p = 311155972145869391293781528370734636009
	q = 315274063651866931016337573625089033553
	with codecs.open(cipherfile) as cipher:
		data = cipher.read()
		ciphertext = base64.b64decode(data)
		while True:
			try:
				print('p * q', math.log(long(p), 2)+math.log(long(q), 2))
				phi = (p - 1) * (q - 1)
				d = gmpy.invert(e, phi)
				key = RSA.construct((long(n), long(e), long(d)))
				PKCS1_v1_5_cipherFormat = PKCS1_v1_5.new(key)
				decrypted = PKCS1_v1_5_cipherFormat.decrypt(ciphertext, 0x64)
				print(decrypted)
				break
			except Exception as ex:
				print(ex)
				p = gmpy.next_prime(p ** 2 + q ** 2)
				q = gmpy.next_prime(2 * p * q)
				e = gmpy.next_prime(e ** 2)
				n = long(p)*long(q)
 
print decrypt_RSA("flag.enc")

# root@BOEING:/kapi/CTF/ACIS-FINAL-2016/rsa# python decrypt.py
# ('p * q', 255.76077963827362)
# Ciphertext with incorrect length.
# ('p * q', 642.4116827637054)
# Ciphertext with incorrect length.
# ('p * q', 1929.253892148807)
# Ciphertext with incorrect length.
# ('p * q', 5790.76167644642)
# Ciphertext with incorrect length.
# ('p * q', 17375.285029339262)
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}
# ASIS{F4ct0R__N_by_it3rat!ng!}







