import requests
from Crypto.Cipher import AES
#from json.decoder import JSONDecodeError

decrypt = '/block_cipher_starter/decrypt/<ciphertext>/'  # is taking ciphertext
encrypt = '/block_cipher_starter/encrypt_flag/'
url = 'http://aes.cryptohack.org'


# send a requests for the encrepted flag

r = requests.get(url+encrypt)
data= r.json()
ciphertext = data['ciphertext']

# send cipher to be decrepted 
r = requests.get(url+decrypt+ciphertext)
data= r.json()
plaintext = data['plaintext']


# decode hex flag and print 
print(bytes.fromhex(plaintext))
