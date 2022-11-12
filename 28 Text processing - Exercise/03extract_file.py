class Extracting:

    def __init__(self, path_name):
        self.path_name = path_name

    def extract_names(self):
        file_and_extension = self.path_name.split('\\')
        file, extension = file_and_extension[-1].split('.')
        return file, extension

    def __repr__(self):
        file_name = self.extract_names()[0]
        file_extension = self.extract_names()[1]
        return f'File name: {file_name}\nFile extension: {file_extension}'


path = input()

extract = Extracting(path)

print(extract)




#################################### TASK CONDITION ############################
"""
                       3.	 Extract File
Write a program that reads the path to a file and subtracts the file name and its extension.

____________________________________________________________________________________________
Example_01

Input
C:\Internal\training-internal\Template.pptx

Output
File name: Template
File extension: pptx

____________________________________________________________________________________________
Example_02

Input
C:\Projects\Data-Structures\LinkedList.cs

Output
File name: LinkedList
File extension: cs

"""
