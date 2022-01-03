#Create mobi's from epubs if not exits

import os
import subprocess

def convert():
	epubs = []
	mobis =[]

	for file in os.listdir(os.getcwd()):
		if file.endswith('.epub'):
			epub = file[:-len('.epub')]
			epubs.append(epub)
		elif file.endswith('mobi'):
			mobi = file[:-len('mobi')]
			mobis.append(mobi)
	#Make a list of epub not in mobis
	converts = []
	for convert in epubs:
		if convert not in mobis:
			inepub = '"'+ convert + '.epub' + '"'
			outmobi = '"'+ convert + '.epub' + '"'
			ebook = 'ebook-convert' + ' ' + inepub

			converts.append(ebook)

	#Run the conversion
	for ebook in converts:
		subprocess.call(ebook, shell=True)


if __name__ == '__main__':
	convert()