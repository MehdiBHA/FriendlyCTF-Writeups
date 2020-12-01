from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import random

def pad(msg):
	while(len(msg) % 16 != 0):
		msg += b'\x00'
	return msg

def getRandomBytes(seed):
	random.seed(seed)
	key = long_to_bytes(random.getrandbits(8*16))
	return key

cipher = b64decode("cNZQNTXpEOevvG28/gXPmQIREF800F2+MmM1ntiEycw=")
for seed in range(0 ,256):
	key = getRandomBytes(seed)	# generate random 16 bytes
	aes = AES.new(key, AES.MODE_ECB)
	flag = aes.decrypt(cipher)
	if b"Securinets{" in flag:
		print(flag)