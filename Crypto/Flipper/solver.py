cipher = list(bytes.fromhex("351b3d18bf41d307d239cc67d02cdd06416be9a57357f9c279e25d51d28ab973"))
# token = "{user_id=[10 digits];is_admin=0}\x01"

block1 = cipher[0:16]
block2 = cipher[16:32]

# The target byte '0' is located at postion 13 of block2
block1[13] = block1[13] ^ ord('0') ^ ord('1')

cipher = block1 + block2

new_cipher = ''.join(chr(i) for i in cipher).encode('latin-1')
print(new_cipher.hex())
