class Caesar:
	def __init__(self,shift):
		self._encoder = [None] * 26
		self._decoder = [None] * 26
		for k in range(26):
			self._encoder[k] = chr((k + shift) % 26 + ord('A'))
			self._decoder[k] = chr((k - shift + 26) % 26 + ord('A'))

	def encrypt(self, message):
		return self.__transform(message, self._encoder)

	def decrypt(self, message):
		return self.__transform(message, self._decoder)

	def __transform(self, original, code):
		msg = list(original)
		for k in range(len(msg)):
			if msg[k].isupper():
				j = ord(msg[k]) - ord('A')
				msg[k] = code[j]
		return ''.join(msg)

if __name__ == '__main__':
	cipher = Caesar(5)
	message = 'DAI JIA YI'
	coded = cipher.encrypt(message)
	print(coded)
	answer = cipher.decrypt(coded)
	print(answer)
