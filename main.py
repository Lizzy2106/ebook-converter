from os import listdir, rename
from os.path import isfile, join
import subprocess

"""Return of the name of file to be kept after conversion.
This just change the extantion .azw3 here
"""
def get_final_filename(file):
	file = file.split(".")
	filename = ".".join(file[0:-1])
	processed_file_name = filename + ".azw3"
	return processed_file_name

""" Return file extension .pdf or epub or mobi
"""
def get_file_extention(file):
	return file.split

ignored_extentions = ["pdf"]

mypath = "/home/lizzy/Dev/ebookConvertor/initaledFiles/"

mypath_converted = "/home/lizzy/Dev/ebookConvertor/convertedFiles/"

mypath_processed = "/home/lizzy/Dev/ebookConvertor/processedFiles/"

raw_files = [file for file in listdir(mypath) if isfile(join(mypath, file))]
converted_files =  [file for file in listdir(mypath_converted) if isfile(join(mypath_converted, file))]

for file in raw_files:
	final_file_name = get_final_filename(file)
	extension = get_file_extention(file)
	print(final_file_name, extension)

	if final_file_name not in converted_files and extension not in ignored_extentions:
		print("Converting : "+file)

		try:
			subprocess.call(["ebook-convert", mypath+file, mypath_converted+final_file_name], shell=True) 
			s = rename(mypath+file, mypath_processed+file)
			print(s)
		except Exception as e:
			raise e
	else:
		print("Already exists : "+final_file_name)