charset = '0123456789abcdef'
keylen = 6

def recurse(width, position, baseString, returnDictionary):
	for char in charset:
		if(position < width - 1):
			recurse(width, position + 1, baseString + char, returnDictionary)
		else:
			returnDictionary.append(baseString + char)

myDictionary = []
recurse(keylen, 0, "", myDictionary) 

print "Dictionary generated"
print type(myDictionary)

for entry in myDictionary:
	print entry
