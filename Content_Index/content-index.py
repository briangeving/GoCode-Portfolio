import string

"""
Content Indexing Engine Capstone Project

You have a bunch of files in the file system!  How can we index these files to make them easily searchable by keyword?

Indexing is a way of moving work 'upfront' so that when the user searches, less work is needed to get them the right search results.

Example index:
index = {'cat':['filename1','filename2','filename3'],'dog':['filename2',filename3]}


Steps 

1) Using your recursive find code, return a list of all the files.
2) Fill out index_all_files function: It takes the list of files, goes through each file, and updates the index appropriately.  It returns the entire index.
3) Fill out find_files_with, it takes the index, and list of keywords. It then returns a list of all the files that have that keyword in it. 

-Note when you index a file throwout all stop words.

Tips:

Look into String module and string.punctuation - http://effbot.org/librarybook/string.htm

Google the set() builtin data type

"""
import os
current_path = "."
stop_words = ['a','an','and','i']
# Optional Extension: Stop words are words that you will ignore in your index, since they are common English words.

file_index = []

def recursive_find(current_path):
    """recursive find all files and return a list of file names"""
	for name in os.listdir(current_path):
		thing = os.path.join(current_path,name)
		file_index.append(thing)
		if os.path.isdir(thing):
			recursive_find(thing)
		else:
			pass	
			#print thing

	return file_index

index = recursive_find(".")

    



def index_all_files(file_list):
    """go through the list of files and add a file's words to the index and return a new index - this section can be as fancy as you want it.  You may want to strip out punctuation, spaces, weird characters.  

    For starters, just work with .txt files.  As an extension, you may want this to work on HTML files."""
    pass


def find_files_with(index,keywords):
    """takes a list of keywords, and return a list of files with those keywords"""
    pass




        

