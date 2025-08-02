#this is what i have so far #This is a python program that will act as a database by reading in raw
# data from a file and store the data in a type of list (tuple, dictionary etc).
# Then the program will analyse the data and return results as answers to some questions.
# The answers will be read to another file (file2).

#------------------Data Reading and Processing------------------#
#First I will open the data file in read mode(r) and read the data.
# I will use utf-8-sig encoding to remove the BOM (Byte Order Mark) issues.
with open('file.txt', 'r', encoding='utf-8-sig') as file:
    f = file.readlines()

#remove escape characters and split the data into a list
newList = []
for line in f:
    newList.append(line.strip().split(','))

# Separate data headers and entries
headers = newList[0]
entries = newList[1:]

print(headers)

# I will convert entries to a list of dictionaries for easier data manipulation
# this is done by zipping the headers with each entry to keep data aligned to its headings.
dictionary = []
for entry in entries:
    dictionary.append(dict(zip(headers, entry)))

#-------------------Data Analysis------------------#
#Questtions to be answered: