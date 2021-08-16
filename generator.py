from function import*


def gen_random_blank_file(path,ext,x):
	for file in range(x):
		newFile = MDP_gen(randint(3,6))
		f = open(path+'/'+newFile+'.'+ext,'w')
		f.close()
		print(f'file: {newFile} generated at [{path}]')
GRBF = gen_random_blank_file


def gen_random_blank_file_with_motif(path,motif,ext,x):
	for file in range(x):
		name = motif+MDP_gen(randint(3,8))
		print(f'creat: {name} at [{path}]')
		f = open(path+'/'+name+'.'+ext,'w')
		f.close()
GRBFWM = gen_random_blank_file_with_motif


def gen_random_file_with_random_data(path,ext,x):
	for file in range(x):
		name = MDP_gen(6)+ext
		print(f'creat {name} at [{path}]')
		f = open(path+'/'+name,'w')
		f.write(MDP_gen(randint(3,10000)))
		f.close()
GRFWRD = gen_random_file_with_random_data


def creat_dir_with_rand_chart(path,x):
	for n in range(x):
		foldername = path+'/'+gen_dir_name()
		print(f'creat {foldername}')
		os.makedirs(foldername, exist_ok=True)
	print('Done')
CDWRC = creat_dir_with_rand_chart


def creat_dir_with_alphabet(path,up):
	if up is True:
		for l in alpha:
			foldername = path+'/'+l.upper()
			print(f'creat: [{foldername}]')
			os.makedirs(foldername, exist_ok=True)
		print('Done')
	elif up is False:
		for l in alpha:
			foldername = path+'/'+l
			print(f'creat: [{foldername}]')
			os.makedirs(foldername, exist_ok=True)
		print('Done')
CDWA = creat_dir_with_alphabet


def creat_dir_with_number(path,x):
	for n in range(x):
		foldername = path+'/'+str(n)
		print(f'creat: [{foldername}]')
		os.makedirs(foldername, exist_ok=True)
	print('Done')
CDWN = creat_dir_with_number


def superGen(path,x):
	for n in range(x):
		print(f'Gen random dirs and files')
		
		foldername = path+'/'+gen_dir_name()
		os.makedirs(foldername, exist_ok=True)
		nbr_file = randint(3,4)

		for file in range(nbr_file):

			f = open(foldername+'/'+MDP_gen(randint(3,10))+'.'+choice(all_ext),'w')
			f.write(gen_rand_long())
			f.close()

			foldername2 = foldername+'/'+gen_dir_name()
			os.makedirs(foldername2, exist_ok=True)

			f2 = open(foldername2+'/'+MDP_gen(randint(3,10))+'.'+choice(all_ext),'w')
			f2.write(gen_rand_long())
			f2.close()

SG = superGen


