import binascii


# return (g, x, y) a*x + b*y = gcd(x, y)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def decryptRSA(p,q,e,ct):
	# compute n
	n = p * q
	phi = (p - 1) * (q - 1)	
	gcd, a, b = egcd(e, phi)
	d = a
	pt = pow(ct, d, n)
	return pt

def encryptRSA(p,q,e,pt):
	# compute n
	n = p * q
	phi = (p - 1) * (q - 1)
	gcd, a, b = egcd(e, phi)
	d = a
	ct = pow(pt, e, n)
	return ct

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def int_to_string(someInt):
	hexadecimals = str(hex(someInt))[2:-1]
	return str(binascii.unhexlify(hexadecimals))

def string_to_int(someStr):
	return int(binascii.hexlify(someStr),16)

def sample(p = 11,q = 13):
	m = 9
	print "m: " + str(m)
	# I set m = 9 because this is an example of RSA calculation. This example use small q and p which produce a small n
	# In encryption and decryption message and cipher will be modulated by n so large integer message/cipher will cause problem.
	
	print "[*] Step 1: Choose p and q"
	print "[*] p = " + str(p)
	print "[*] q = " + str(q)

	n = p * q

	print "\n[*] Step 2: Calculate the modulus n"
	print "[*] n = p*q"
	print "[*] n = " + str(p) + " * " + str(q)
	print "[*] n = " + str(n)

	phi = (p-1) * (q-1)

	print "\n[*] Step 3: Calculate totient phi(n)"
	print "[*] phi(n) = (p-1) * (q-1)"
	print "[*] phi("+str(n)+") = (" + str(p-1) + ") x (" + str(q-1) + ")"
	print "[*] phi("+str(n)+") = " + str(phi)

	
	e_arr = []
	for e in xrange(1,phi+1):
		g, x, y = egcd(e,phi)
		if g == 1 and e != 1:
			e_arr.append(e)
	e = e_arr[0]
	print "\n[*] Step 4: Choose the public exponent e"
	print "[*] 1 < e < phi(n) and gcd(e,phi(n)) = 1"
	print "[*] 5 possible e: " + str(e_arr[0:5])
	print "[*] Let's choose the 1st"
	print "[*] e = " + str(e)

	d = mulinv(e,phi)

	print "\n[*] Step 5: Choose the private exponent d"
	print "[*] 1 < d < phi(n) and ed = 1 mod phi(n)"
	print "[*] d = 1/e mod phi(n)"
	print "[*] d = (multiplicative inverse of e) mod phi(n)"
	print "[*] The line above means e*d mod phi(n) = 1 and d is the largest possible value"
	print "[*] d: " + str(d)

	print "\n[*] ### Summary ###"
	print "[*] p = " + str(p)
	print "[*] q = " + str(q)
	print "[*] n = " + str(n)
	print "[*] e = " + str(e)
	print "[*] d = " + str(d)
	print "[*] m = " + str(m)

	c = pow(m,e,n)

	print "\n[*] Step 6: Encryption"
	print "[*] c = m^e mod n"
	print "[*] c = pow(m,e,n)"
	print "[*] c = pow(" + str(m) + "," + str(e) + "," + str(n) + ")"
	print "[*] c = " + str(c)

	m = pow(c,d,n)

	print "\n[*] Step 7: Decryption"
	print "[*] m = c^d mod n"
	print "[*] m = pow(c,d,n)"
	print "[*] m = pow(" + str(c) + "," + str(d) + "," + str(n) + ")"
	print "[*] m = " + str(m)

if __name__ == "__main__":
	sample()
