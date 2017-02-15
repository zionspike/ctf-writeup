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