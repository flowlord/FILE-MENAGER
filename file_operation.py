from function import*


def scan_file(path):
	nbr = 0
	t = 0
	for root, dire, files in os.walk(path):
		for name in files:
			ph = norm(root,name)
			print("file find at ["+ph+"]")
			nbr = nbr+1

	print(f'\n {nbr} files find\n')


def find_file_by_name(path,file_name):
	nbr = 0
	t = 0
	for root, dire, files in os.walk(path):
		for name in files:
			if getFileName(name) == file_name:
				ph = norm(root,name)
				print(f'file: {name} find at [{ph}]')
				nbr +=1
			else:
				pass

			t +=1
	print(f'\nfile find {nbr} time , ({round(nbr*100/t)}%)\n')


def inject_text_at_start_file(path,file_name,text):
	nbr = 0

	for root, dire, files in os.walk(path):
		for name in files:
			if name == file_name:
				ph = norm(root,name)

				add_text_in_start(ph,text)

				print("$ inject : " + "'" +text+ "'" + " in [" + ph +"]")
				nbr +=1

	print(f'\ntext: "{text}" added {nbr} time\n')


def inject_text_at_end_file(path,file_name,text):
	nbr = 0

	for root, dire, files in os.walk(path):
		for name in files:
			if name == file_name:
				ph = norm(root,name)

				add_text_in_end(ph,text)

				print("$ add : " + "'" +text+ "'" + " in [" + ph +"]")
				nbr +=1
			else:
				pass

	print(f'\ntext: "{text}" added {nbr} time\n')


def remove_file_by_name(path,file_name):
	nbr = 0
	t = 0
	for root, dire, files in os.walk(path):
		for name in files:
			if name == file_name:
				ph = norm(root,name)
				print(f'file: {name} removed at [{ph}]')
				os.remove(ph)
				nbr +=1
			else:
				pass

			t +=1
	print(f'\nfile removed {nbr} time , ({round(nbr*100/t)}%)\n')


def rename_file(path,file_name,new_filename):
	nbr = 0
	t = 0
	for root, dire, files in os.walk(path):
		for name in files:
			if name == file_name:
				ph = norm(root,name)
				ph2 = f'{os.path.join(root,new_filename)}'.replace('\\','/')
				print(f'file: {name} renamed at [{ph}]')
				os.rename(ph,ph2)
				nbr +=1
			else:
				pass

			t +=1
	print(f'\nfile renamed {nbr} time , ({round(nbr*100/t)}%)\n')


def duplic_file(file):
	file_name = getFileName(file)
	ext = getExtFile(file)

	file = open(file,'rb')
	read_file = file.readlines()

	dup_file = open(file_name + ' (clone).' +ext,'wb')

	for data in read_file:
		dup_file.write(data)

	dup_file.close()

	file.close()

	print('Done !')


def remove_file_with_motif(path,motif):
	nbr = 0

	for root, dire, files in os.walk(path):
		for name in files:
			if IfMotif(name,motif) is True:
				ph = norm(root,name)
				print(f'file: {name} remove at [{ph}]')
				os.remove(ph)
				nbr +=1
			else:
				pass

	print(f'\n {nbr} files removed \n')

