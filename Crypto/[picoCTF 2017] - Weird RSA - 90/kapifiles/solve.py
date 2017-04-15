import binascii
import struct

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
	print "d: " + str(d)
	pt = pow(ct, d, n)
	return pt

def encryptRSA(p,q,e,pt):
	# compute n
	n = p * q
	phi = (p - 1) * (q - 1)
	gcd, a, b = egcd(e, phi)
	d = a
	print "d: " + str(d)
	ct = pow(pt, e, n)
	return ct


def convert(int_value):
   encoded = format(int_value, 'x')
   length = len(encoded)
   encoded = encoded.zfill(length+length%2)
   return encoded.decode('hex')

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def main():
	# By implementing Chinese remainder algorithm
	# 1) p and q are the primes
	# 2) dp = d mod (p - 1)
	# 3) dq = d mod (q - 1)
	# 4) Qinv = 1/q mod p *This is not integer devision but multiplicative inverse
	# 5) m1 = pow(c, dp, p)
	# 6) m2 = pow(c, dq, q)
	# 7-1) h = Qinv(m1 - m2) mod p  ; if m1 < m2
	# 7-2) h = Qinv * (m1 + q/p) 
	# 8) m = m2 + hq

	# m = 65
	# p = 61
	# q = 53
	# dp = 53
	# dq = 49
	# c = 2790

	p = 11387480584909854985125335848240384226653929942757756384489381242206157197986555243995335158328781970310603060671486688856263776452654268043936036556215243
	q = 12972222875218086547425818961477257915105515705982283726851833508079600460542479267972050216838604649742870515200462359007315431848784163790312424462439629
	dp = 8191957726161111880866028229950166742224147653136894248088678244548815086744810656765529876284622829884409590596114090872889522887052772791407131880103961
	dq = 3570695757580148093370242608506191464756425954703930236924583065811730548932270595568088372441809535917032142349986828862994856575730078580414026791444659
	c = 95272795986475189505518980251137003509292621140166383887854853863720692420204142448424074834657149326853553097626486371206617513769930277580823116437975487148956107509247564965652417450550680181691869432067892028368985007229633943149091684419834136214793476910417359537696632874045272326665036717324623992885

	Qinv = mulinv(q,p)
	print "Qinv: " + str(Qinv)

	m1 = pow(c, dp, p)
	print "m1: " + str(m1)

	m2 = pow(c, dq, q)
	print "m2: " + str(m2)

	h = (Qinv * (m1 - m2)) % p
	print "h: " + str(h)

	m = m2 + (h*q)
	print "m: " + str(int(m))

	hexadecimals = str(hex(m))[2:-1]
	print "solved: " + str(binascii.unhexlify(hexadecimals))
	# solved: Theres_more_than_one_way_to_RSA

if __name__ == "__main__":
	main()


# http://crypto.stackexchange.com/questions/19413/what-are-dp-and-dq-in-encryption-by-rsa-in-c
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Using_the_Chinese_remainder_algorithm
# https://zzundel.blogspot.com/2011/02/rsa-implementation-using-python.html