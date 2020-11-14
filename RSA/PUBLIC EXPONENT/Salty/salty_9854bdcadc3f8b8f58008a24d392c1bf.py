import binascii
from sympy.ntheory import factorint

print("RSA Level 7")

n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767                                                                  
e = 65537
ciphertext = 44981230718212183604274785925793145442655465025264554046028251311164494127485

#Use the private key that you found for these parameters in the previous challenge to decrypt this ciphertext:

ciphertext = 77578995801157823671636298847186723593814843845525223303932
# factorization 
p, q = factorint(n)

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
    return x

phi = (p-1)*(q-1)
print('phi:', phi)

# Compute modular inverse of e
d = egcd(e, phi)
print('d:', d)

# try to decrypt
decrypted_dec = pow(ciphertext, d, n)

# convert from decimal to string
decrypted_message = binascii.unhexlify(hex(decrypted_dec)[2:]).decode()

  # [2:] remove 0x from beginning

print('decrypted message:', decrypted_message)
