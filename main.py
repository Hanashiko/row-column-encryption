import math

key1 = input("Ключ 1: ").upper()
key2 = input("Ключ 2: ").upper()

key = ''.join(sorted(set(key1 + key2)))

def encryptMessage(msg):
	cipher = ""

	k_indx = 0

	msg_len = float(len(msg))
	msg_lst = list(msg)
	key_lst = sorted(list(key))

	col = len(key)
	
	row = int(math.ceil(msg_len / col))

	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)

	matrix = [msg_lst[i: i + col] 
			for i in range(0, len(msg_lst), col)]

	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx] 
						for row in matrix])
		k_indx += 1

	return cipher.replace("_","")

msg = inpt("Текст: ").upper()

cipher = encryptMessage(msg)
print("Зашифрований текст: {}".
			format(cipher))
