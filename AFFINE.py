# Group 4: Tong Cong Binh - Tran Huu Duy - Do Trung Hieu

# Extended Euclidean Algorithm for finding modular inverse
def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None # modular inverse does not exist
	else:
		return x % m

# Affine cipher encryption function and returns the cipher text
def affine_encrypt(text, key):
	#E(P, k) = (a*P + b) % 26
	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ])

# Affine cipher decryption function and returns original text
def affine_decrypt(cipher, key):
	#D(C, k) = a^-1 (C - b) % 26
	return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ])
