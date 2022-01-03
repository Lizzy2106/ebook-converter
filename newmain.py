#!/usr/bin/python
#
#jmeb @ May 2011
#A very first attempt at python scripting
#
#Create mobi's from epubs if not already present
#
 
import os
import subprocess
import sys
 
def main():
 
#Generate two lists: one .epub, one .mobis
  epubs = []
  mobis = []
 
  for filename in os.listdir(os.getcwd()):
    if filename.endswith('.epub'):
      epub = filename[:-len('.epub')]
      epubs.append(epub)
    elif filename.endswith('.mobi'):
      mobi = filename[:-len('.mobi')]
      mobis.append(mobi)
 
#Make a list of epub not in mobis
  converts = []
  for convert in epubs:
    if convert not in mobis:
      #Some hackish processing to write shell commands into list
      inepub = '"' + convert + '.epub' + '"'
      outmobi = '"' + convert + '.mobi'  + '"'
      ebook = 'ebook-convert' + ' ' + inepub + ' ' + outmobi
      #Generate list of shell commands to run
      converts.append(ebook)
 
#Run the conversions
  for ebook in converts:
    subprocess.call(ebook, shell=True)
 
if __name__ == '__main__':
    main()