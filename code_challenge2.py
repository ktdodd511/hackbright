def decode(word):
	return word[::3]

word = raw_input('Enter the encrypted word:')

print decode(word)
