from function import*


def scan_dir(path):
	n = 0
	for root, dirs, files in os.walk(path):
		for rep in dirs:
			print(f'find: {rep}')
			n = n+1

	print(f'\nTotal: {n} floder\n')


def find_dir_by_name(path,dirname):
	nbr = 0
	t = 0
	for root, dirs, files in os.walk(path):
		for rep in dirs:
			if rep == dirname:
				ph = norm(root,rep)
				print(ph)
				nbr +=1
			else:
				pass

			t +=1
	print(f'\nDirectory name find in {nbr} time\n')


def creat_dir(path,foldername):
	os.makedirs(path+'/'+foldername, exist_ok=True)


def creat_dir_with_motif(path,motif,x):
	c = 0
	for n in range(x):
		foldername = path+'/'+motif+str(c)
		print(f'creat {motif+str(c)}')
		os.makedirs(foldername, exist_ok=True)
		c = c+1
	print('Done')


def clone_dir(path):
	shutil.copytree(path,get_dir_name(path)+' (clone)')
	print(f'dir: {get_dir_name(path)} cloned')



# DANGER ZONE !! ----------------------------------------------------

def remove_empty_folder(path):
	t = 0
	for root, dirs, files in os.walk(path):
		for rep in dirs:
			ph = norm(root,rep)
			try:
				print(f' RIP: [{ph}]')
				os.rmdir(ph)
				t +=1
			except OSError:
				pass

	print(f'\n Total {t} empty folder removed\n')


def remove_empty_folder_by_name(path,dirname):
	nbr = 0
	t = 0
	for root, dirs, files in os.walk(path):
		for rep in dirs:
			if rep == dirname:
				ph = norm(root,rep)
				try:
					print(f' RIP: [{ph}]')
					os.rmdir(ph)
					nbr +=1
				except OSError:
					pass
			else:
				pass

	print(f'\nDirectory name find in {nbr} time\n')

