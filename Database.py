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
    
#example output
#for entry in dictionary:
    #print(entry['CityName'])

#-------------------Data Analysis------------------#
#Questions to be answered:
#A. How many countries have names ending with 'a'?
def count_countries_ending_with_a(dictionary):
    countryset = set()  # Set to store unique country names
    count = 0

    for entry in dictionary:
        country = entry['CountryName']
        if country.endswith('a') and country not in countryset:
            countryset.add(country)
            count += 1

    return count


#D.
def count_countries_independent(dictionary):
    independent_countries = set()
    yearcount = 0

    for entry in dictionary:
        year = entry.get('IndepYear')
        country = entry.get('CountryName')

        if year is None or year == 'NULL' or year == '':
            continue
        year = int(entry['IndepYear'])
        # Check if year is an int before comparing
        #print(isinstance(year, int), year, country)  # Debugging line to check types
    # Ensure year is an integer before comparing
        if isinstance(year, int):
            if 1960 <= year <= 1980:
                if country not in independent_countries:
                    independent_countries.add(country)
                    yearcount += 1
    print(f"Total unique countries that gained independence between 1960 and 1980: {yearcount}")

    return yearcount
#E
def name_countries_independent(dictionary):
    independent_countries = set()
    yearcount = 0

    for entry in dictionary:
        year = entry.get('IndepYear')
        country = entry.get('CountryName')

        if year is None or year == 'NULL' or year == '':
            continue
        year = int(entry['IndepYear'])
        # Check if year is an int before comparing
        #print(isinstance(year, int), year, country)  # Debugging line to check types
    # Ensure year is an integer before comparing
        if isinstance(year, int):
            if 1830 <= year <= 1850:
                if country not in independent_countries:
                    independent_countries.add(country)
                    yearcount += 1
    print(independent_countries)
    print(f"Naming the countries that gained independence between 1830 and 1850: {yearcount}")
    return yearcount

#H.
def count_countries_ending_with_a(dictionary):
    countryset = set()  # Set to store unique country names
    count = 0

    for entry in dictionary:
        country = entry['CountryName']
        if country.endswith('a') and country not in countryset:
            countryset.add('CountryName')

    print(countryset)
    return list(countryset)

#F
def top(dictionary):
    lifeExpectancyset = set()  # Set to store unique country names
    count = 0

    for entry in dictionary:
        lifeExpectancy = entry['LifeExpectancy']

        if lifeExpectancy is None or lifeExpectancy == 'NULL' or lifeExpectancy == '':
            continue
        lifeExpectancyset.add(lifeExpectancy)
    top5 = sorted(lifeExpectancyset, reverse=True)[:5]
    print(top5)
    return count

#G
def lang(dictionary):
    langlist = list()  # Set to store unique country names
    count = 0

    for entry in dictionary:
        language = entry['Language']

        if language is None or language == 'NULL' or language == '':
            continue
        langlist.append(language)
        count = langlist.count(language)
        print('Language: ' + language + ', Count: ' + str(count))

    
    return count
lang(dictionary)
