import sys, time
from subprocess import Popen, PIPE, STDOUT

def check(startString):
	foundSTR = ""
	for x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-{}":
		findingSTR = startString + x
		process = Popen(["./re2", findingSTR], stdout=PIPE, stdin=PIPE, stderr=PIPE)
		(output, err) = process.communicate(input="")
		if not "Better luck" in output:
			foundSTR = x
			print "Found : " + str(x)
			break
	return foundSTR

flag = ""
while True:
	flag = flag + check(flag)
	print "Flag: " + flag
	if flag[-1] == "}":
		break
