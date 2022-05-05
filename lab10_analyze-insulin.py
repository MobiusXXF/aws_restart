print("**Preparing to Analyze Insulin with Python")
print(" ")

print("--Retreiving the protein sequence of human preproinsulin:")
print(" ")

import re
from pathlib import Path

#Function that takes the file path, name and data and writes to file
def WriteToFile(path, file_name, file_data):
    #print file lenght and data to screen for accuracy confirmation
    print(f'{len(file_data)}: {file_data}')
    with open(f'{path}/{file_name}', 'w') as f:
        f.write(file_data)
        f.close()

    
#Create a new directory for the files to be saved into
p = Path('files/insulin_files')
#To prevent an exception occuring if dir already exists: exist_ok=True 
p.mkdir(exist_ok=True)

#Open txt file and save all contents to file_text variable
with open('files/preproinsulin-seq.txt') as f:
    file_text = f.read()

print(file_text)

#Regex is uses to clean the text, Negation is used and result is stored to cleaned_text
#Substitute all characters that do not match lowercase a-z  with '' which essentially deletes the character
cleaned_text = re.sub(r'[^a-z]','' , file_text)

#Saves cleaned_text to a new txt file
WriteToFile(p, 'preproinsulin-seq-clean.txt', cleaned_text)

#Saves characters from the cleaned_text to a new txt file using slicing
#Collections are 0 based and go up to but not including the second number
WriteToFile(p, 'lsinsulin-seq-clean.txt', cleaned_text[:24])
WriteToFile(p, 'binsulin-seq-clean.txt', cleaned_text[24:54])
WriteToFile(p, 'cinsulin-seq-clean.txt', cleaned_text[54:89])
WriteToFile(p, 'ainsulin-seq-clean.txt', cleaned_text[89:])