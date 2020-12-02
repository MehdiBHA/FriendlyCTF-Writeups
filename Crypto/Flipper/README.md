# Flipper
![Flipper](https://user-images.githubusercontent.com/62826765/100810414-c3a33c80-3438-11eb-89fd-dcf7e12faeb8.png)

Its **AES-CBC** challenge, we were given a source code and a server netcat (I'm going to do the writeup on local) :
```python
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import random
import os

print("\n------------ Welcome To Flipper ------------\n")

KEY = os.urandom(16)
IV = os.urandom(16)

def getFlag(token):
    dec = decrypt(token)
    if b"admin=1" in dec:
        flag = open('flag.txt','r+').read().strip()
        print("Welcome Admin ! Here is your flag : "+flag)
        exit()
    raise Exception

def encrypt(msg):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    msg = pad(msg.encode(), 16)
    enc = cipher.encrypt(msg)
    return enc.hex()

def decrypt(msg):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    dec = cipher.decrypt(bytes.fromhex(msg))
    dec = unpad(dec, 16)
    return dec


while True:
    print("Choose an option :")
    print("[1] Generate Token")
    print("[2] Get Flag")
    ans = input(">> ")

    if ans == "1":
        id = random.randint(2**30,2**32)
        token = "{user_id="+str(id)+";is_admin=0}"
        print("Here is your token : "+encrypt(token)+"\n")

    elif ans == "2":
        print("Enter your token :")
        token = input(">> ")
        try:
            getFlag(token)
        except Exception:
            print("You have to be an ADMIN to get the flag !")
            exit()
```


## Attack
First, have a look at the [AES-CBC mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC))

CBC mode had a vulnerability that in encryption (or decryption) it uses the previous block to XOR it with next block. Then since I’m in control of what’s get decrypted, then I’m in control of the previous encrypted block, which means what’s going to be XORed with the current decrypted block.

So think about it, if we flip some bits of the previous ciphertext block, the next plaintext block plaintext will change according to what bits you flip. 

![082113_1459_CBCByteFlip3](https://user-images.githubusercontent.com/62826765/100911065-09124900-34cf-11eb-8765-81f98f3e9517.jpg)

And that's what called **_AES-CBC Bit-Flipping Attack_**

## Exploit
Honestly, it's rough to write a full explication of the attack :) so I leave you this with [Link](https://resources.infosecinstitute.com/topic/cbc-byte-flipping-attack-101-approach/) go check it.

We take an exemple for the exploit :

_token = "{user_id=2219801953;is_admin=0}\x01"_

_cipher = "d8c3cf10da63d5824497e45b7293eb030c484282245efbe157d801837f064497"_

Our exploit :
```python

```


