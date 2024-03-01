import hashlib
filename = 'image.jpeg'

with open(filename, "rb") as f:
	file_data = f.read()
	result = hashlib.sha3_256(file_data).hexdigest()
	print(result)