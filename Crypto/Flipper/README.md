# Flipper
![Flipper](https://user-images.githubusercontent.com/62826765/100810414-c3a33c80-3438-11eb-89fd-dcf7e12faeb8.png)

Its **AES-CBC** challenge, we were given a source code and a server netcat :
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
After connecting, it gives us two options. We choose ```1``` it gives us a token, but when we try to get the flag with it a message says : ```You have to be an ADMIN to get the flag !```

![2020-12-02 20_38_38-Kali - VMware Workstation](https://user-images.githubusercontent.com/62826765/100922613-64980300-34de-11eb-8eea-4e9b24e0faa0.png)

After looking at the source code, we see that it checks for the existence of "_admin=1_" after the decryption :
```python
if b"admin=1" in dec:
        flag = open('flag.txt','r+').read().strip()
        print("Welcome Admin ! Here is your flag : "+flag)
        exit()
```
But the problem is that we have "_admin=0_" in our token ! So how we are going to make "_admin=1_" appears ?

With digging on AES attacks and according to the challenge description, this leads us to **_AES-CBC Bit-Flipping Attack_**.

## Attack
First, have a look at the [AES-CBC mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)).

CBC mode had a vulnerability that in encryption (or decryption) it uses the previous block to XOR it with next block. Then since I’m in control of what’s get decrypted, then I’m in control of the previous encrypted block, which means what’s going to be XORed with the current decrypted block.

So think about it, if we flip some bits of the previous ciphertext block, the next plaintext block plaintext will change according to what bits you flip. 

![082113_1459_CBCByteFlip3](https://user-images.githubusercontent.com/62826765/100911065-09124900-34cf-11eb-8765-81f98f3e9517.jpg)

## Exploit
Honestly, it's rough to write a full explication of the attack :) so I leave you this with [Link](https://resources.infosecinstitute.com/topic/cbc-byte-flipping-attack-101-approach/) go check it.

We take an exemple for the exploit :

```cipher = "351b3d18bf41d307d239cc67d02ddd06416be9a57357f9c279e25d51d28ab973```

Our exploit :
```python
cipher = list(bytes.fromhex("351b3d18bf41d307d239cc67d02cdd06416be9a57357f9c279e25d51d28ab973"))
# token = "{user_id=[10 digits];is_admin=0}\x01"

block1 = cipher[0:16]
block2 = cipher[16:32]

# The target byte '0' is located at postion 13 of block2
block1[13] = block1[13] ^ ord('0') ^ ord('1')

cipher = block1 + block2

new_cipher = ''.join(chr(i) for i in cipher).encode('latin-1')
print(new_cipher.hex())
```
![Sol](https://user-images.githubusercontent.com/62826765/100921682-2fd77c00-34dd-11eb-9c59-1c69a6541325.png)

FLAG is **_Securinets{Rijndael_is_pr0ud}_**


