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
