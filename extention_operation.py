from function import*


def scan_file_by_ext(path,extname):
	nbr = 0
	ne = 0
	t = 0
	for root, dire, files in os.walk(path):
		for name in files:
			if getFileName(name) == extname:
				ph = norm(root,name)
				print(f'file: {name} find at {ph}')
				nbr +=1
			else:
				ne +=1
			t +=1
	
	print(f'\n{nbr} file{extname} find / {ne} , ({round(nbr*100/t)}%)\n')


def scan_file_by_lst_ext(path,lst_extname):
	nbr = 0

	for root, dire, files in os.walk(path):
		for name in files:
			if getExtFile(name) in lst_extname:
				ph = norm(root,name)
				print(f'find: {getExtFile(name)} at [{ph}]')
				nbr +=1
	
	print(f'\n{nbr} file extention find\n')


def scan_all_ext_file(path):
	nbr = 0
	ne = 0
	i = 0

	ext_find = []
	unknown_ext = []

	for root, dire, files in os.walk(path):
		for name in files:
			if ifExtention(name) is True:
				ph = norm(root,name)
				fex = getExtFile(name)

				if fex in ext_find:
					pass
				else:
					print(f'{i}) find .{fex} at [{ph}]\n')
					ext_find = ext_find + [fex]
					nbr = nbr+1
					i = i+1
			elif ifExtention(name) is False:
				unknown_ext = unknown_ext + [name]
				ne = ne +1

	print(f'\nTotale {nbr} extention file scaned\n')
	print(f'{ext_find}\n')

	print('-----------------------------------------------------\n')

	print(f'Totale {ne} unknown extention file scaned')
	print(f'{unknown_ext}\n')

	print(f'Totale {nbr+ne} extention file scaned \n')


def copy_file_by_ext(path,des,lst_extname):
	nbr = 0

	for root, dire, files in os.walk(path):
		for name in files:
			if getExtFile(name) in lst_extname:
				ph = norm(root,name)
				
				try:
					print(f'$COPY: {name} to [{des}]')
					shutil.copy(ph,des)
				except OSError:
					print(f'$COPY: {name} to [{des}]')
					shutil.copy(name,des)

				nbr +=1
	
	print(f'\n{nbr} file copied\n')


def copy_all_file_ext(path,des):
	nbr = 0

	for root, dire, files in os.walk(path):
		for name in files:
			ph = norm(root,name)
			
			try:
				print(f'$COPY: {name} to [{des}]')
				shutil.copy(ph,des)
			except OSError:
				print(f'$COPY: {name} to [{des}]')
				shutil.copy(name,des)

			nbr +=1
	
	print(f'\n{nbr} file copied\n')


# DANGEROUS ZONE ----------------------------------------------------------

# RENAME ALL FILE IN THE PATH

def rename_file_ext(path,new_ext):
	nbr = 0
	for root,dirs,files in os.walk(path):
		for name in files:
			ph = norm(root,name)
			renamedFile = getFileName(name)+'.'+new_ext
			path_newfile = norm(root,renamedFile)
			os.rename(ph,path_newfile)
			print(f'file: {ph} ---> [{path_newfile}]')
			nbr = nbr+1
	print(f'{nbr} renamed.')


def rename_ext_with_ext(path,old_ext,new_ext):
	old_ext = old_ext.replace('.','')
	nbr = 0
	for root,dirs,files in os.walk(path):
		for name in files:
			if getExtFile(name) == old_ext:
				ph = norm(root,name)
				renamedFile = getFileName(name)+'.'+new_ext
				path_newfile = norm(root,renamedFile)

				os.rename(ph,path_newfile)
				print(f'file: {ph} ---> [{path_newfile}]')
				nbr = nbr+1
	print(f'{nbr} file renamed.')



def rename_file_ext_with_lst(path,old_ext_lst,new_ext):
	tmp = []
	for ext in old_ext_lst:
		tmp = tmp + [ext.replace('.','')]

	old_ext_lst = tmp

	nbr = 0
	for root,dirs,files in os.walk(path):
		for name in files:
			if getExtFile(name) in old_ext_lst:
				ph = norm(root,name)
				renamedFile = getFileName(name)+'.'+new_ext
				path_newfile = norm(root,renamedFile)
				
				os.rename(ph,path_newfile)
				print(f'file: {ph} ---> [{path_newfile}]')
				nbr = nbr+1
	print(f'{nbr} renamed.')


def rename_file_if_no_ext(path):
	ne = 0
	for root, dire, files in os.walk(path):
		for name in files:
			ph = norm(root,name)
			path_newfile = norm(root,name+'.unk')
			if ifExtention(name) is False:
				os.rename(ph,path_newfile)
				ne = ne +1
				print(f'file: {name} renamed to .unk')
	print(f'{ne} file renamed to .unk')


def remove_unk_file(path):
	ne = 0
	for root, dire, files in os.walk(path):
		for name in files:
			ph = norm(root,name)
			if getExtFile(name) == 'unk':
				os.remove(ph)
				ne = ne +1
				print(f'file: {name} removed at [{ph}]')
	print(f'{ne} files removed')


def remove_file_by_ext_lst(path,extname_lst):
	nbr = 0
	for root, dire, files in os.walk(path):
		for name in files:
			if getExtFile(name) in extname_lst:
				ph = norm(root,name)
				print(ph,' is death')
				os.remove(ph)
				nbr +=1
			else:
				pass

	print(f'\n{nbr} files removed')


def remove_all_ext(path):
	nbr = 0
	for root, dire, files in os.walk(path):
		for name in files:
			ph = norm(root,name)
			print(ph,' is death')
			os.remove(ph)
			nbr +=1
	print(f'\n{nbr} files removed')


