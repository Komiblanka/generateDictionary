import itertools

charset = '0123456789abcdef'
keylen = 6

for c in itertools.product(charset, repeat=6):
	password = ''.join(c)
	print password

