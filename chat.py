def read_file(filename):
	chat = []
	name = 'name'
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			if line.strip() == 'Allen' or line.strip() == 'Tom':
				name = line.strip()
				continue
			else:
				chat.append(name+ ':' + line)
	return chat


def add_file(filename, chat):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for c in chat:
			f.write(c)

read_file('input.txt')
print(read_file('input.txt'))
add_file('output.txt', read_file('input.txt'))