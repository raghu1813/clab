from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(b'raghuram')
print(ciphertext)
res,ta=cipher.decrypt_and_verify(b'\xd5Q\x8a;\xce\xbf_\x9a',tag)
print(res)

