import sys
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


if __name__ == '__main__':
	cipher = open("flag.enc", "r").read()
	key = open("priv.key", "r").read()
	rsakey = RSA.importKey(key)
	rsakey = PKCS1_OAEP.new(rsakey)
	decrypted = rsakey.decrypt(base64.b64decode(cipher))
	print decrypted
