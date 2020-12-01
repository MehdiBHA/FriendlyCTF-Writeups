from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import random

flag = b"TODO"

def pad(msg):
	while(len(msg) % 16 != 0):
		msg += b'\x00'
	return msg

def getRandomBytes(seed):
	random.seed(seed)
	key = long_to_bytes(random.getrandbits(8*16))
	return key

seed = random.randrange(0,256)
key = getRandomBytes(seed)	# generate random 16 bytes
flag = pad(flag)
aes = AES.new(key, AES.MODE_ECB)
cipher = aes.encrypt(flag)
print(b64encode(cipher))

'''
cipher = "cNZQNTXpEOevvG28/gXPmQIREF800F2+MmM1ntiEycw="
'''