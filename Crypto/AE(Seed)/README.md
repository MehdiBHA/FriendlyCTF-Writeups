# AE(Seed)
![Aeseed](https://user-images.githubusercontent.com/62826765/100807612-f1858280-3432-11eb-808c-aa03b61cbc11.png)

Its **AES-ECB** challenge, we were given a source code :
```python
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
```

## Attack
According to the title of the challenge, we see that it's something related to [Seed Function](https://www.w3schools.com/python/ref_random_seed.asp#:~:text=The%20seed()%20method%20is,uses%20the%20current%20system%20time.).

What the seed function does is initialising a pseudo-random number generator with given number to start with (seed value), which means that anyone seeds with the same value will get the same random sequence.

So all we have to do is to find the correct seed value so we can generate the correct key and decrypt the cipher.

## Exploit
In our given source code we see this line :
```python
seed = random.randrange(0,256)
```
So the seed value is a random number between 0 and 256. With a little bruteforce we can find the correct one.
```python
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
```

FLAG is **_Securinets{never_seed_your_key}_**
