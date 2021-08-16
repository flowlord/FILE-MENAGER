from random import choice,randint
import os
import shutil


img_ext = ['png','jpeg','jpg','gif','ico','svg','webp','webmp','tiff','tga','bmp','eps','hdr','exr','tif','tiff','bmp','raw']

text_ext = ['txt','rtf','html','htm','jar','css','js','php','p','c','cpp','sql','vbs','pl','h','class','py','xml','json','dex','log']

video_ext = ['mp4','avi','mov','mkv','webm','flv']

audio_ext = ['mp3','wav','midi','ogg','m4a']

app_ext = ['exe','msi','apk','com','bat']

doc_ext = ['pdf','doc','docx','ppt','pub','xls','pptx','xlsx']

compress_ext = ['zip','rar','tar','tgz','gz','cab','arc','ace']

police_ext = ['ttf','otf','eot','woff','woff2']

tmp_ext = ['tmp']

url_ext = ['url','link']

apk_file_dezip_ext = ['arsc','so']

all_ext = img_ext + text_ext + video_ext + audio_ext + app_ext + doc_ext + compress_ext + police_ext + tmp_ext + url_ext


alpha = list('abcdefghijklmnopqrstuvwxyz')

def norm(root,name):
	return f"{os.path.join(root,name)}".replace('\\','/')

def MDP_gen(longueur):
	psw = ""
	pattern = '_azerty uiopq sdfghjklm-wxcvbn1 234567890'
	for element in range(longueur):
		psw = psw + choice(pattern)
	return psw

def gen_dir_name():
	longueur = randint(3,10)
	psw = ""
	pattern = '_azerty uiopqsdfghjklmwxcvbn1234567890'
	for element in range(longueur):
		psw = psw + choice(pattern)
	return psw

def MDP_genForDupliFile():
	psw = ""
	pattern = 'azertyuiopqsdfghjklmwxcvbn'
	for element in range(4):
		psw = psw + choice(pattern)
	return '_'+psw+'.'


def gen_rand_long():
	longueur = randint(3,999999)
	psw = ""
	pattern = '_$--------azerty uiopq sdfghjklmwxcvbn1AZERTY UIOPQ SDFGHJKLMWXCVBN1 234567890'
	for element in range(longueur):
		psw = psw + choice(pattern)
	return psw

def revtext(text):
	new_txt = ''
	for e in reversed(text):
		new_txt = new_txt+e
	return new_txt

def ifExtention(filename):
	if len(filename.split('.')) == 1:
		return False
	else:
		return True

def getExtFile(filename):
	if len(filename.split('.')) == 1:
		return 'unk'
	else:
		return filename.split('.')[-1]

def getFileName(filename):
	filename = filename.replace('\\','/')
	filename = filename.split('.')[0]
	filename = filename.split('/')[-1]
	return filename

def get_dir_name(dirname):
	dirname = dirname.split('/')
	ndn = []
	for e in dirname:
		if e == '':
			pass
		else:
			ndn = ndn + [e]
	ndn = ndn[-1]
	return ndn


# if motif is present at least one
# file.txt, e ---> True
# file.txt, le ---> True
# file.txt, e.t ---> True


def IfMotif(filename,motif):
	if motif not in filename:
		return False
	return True


def IfPrefix(filename,motif):
	filename = filename[:len(motif)]
	return (filename == motif)


def IfSuffix(filename,motif):
	filename = filename.split('.')[0]

	filename = revtext(filename)
	motif = revtext(motif)

	filename = filename[:len(motif)]

	return (filename == motif)


def add_text_in_start(file,text):
	read_file = open(file,'r').readlines()

	file = open(file,'w')

	file.write(text)
	file.write('\n')

	for line in read_file:
		file.write(line)

	file.close()


def add_text_in_end(file,text):
	file = open(file,'a')
	file.write(text)
	file.close()

