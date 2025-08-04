#this is what i have so far #This is a python program that will act as a database by reading in raw
# data from a file and store the data in a type of list (tuple, dictionary etc).
# Then the program will analyse the data and return results as answers to some questions.
# The answers will be read to another file (file2).

#------------------Data Reading and Processing------------------#
#First I will open the data file in read mode(r) and read the data.
# I will use utf-8-sig encoding to remove the BOM (Byte Order Mark) issues.
from itertools import count


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
#-------------------------------------------------------------------------------------------------------------
#A. How many countries have names ending with 'a'?
def count_countries_ending_with_a(dictionary):
    countryset = set()  # Set to store unique country names
    count = 0

    for entry in dictionary:
        country = entry['CountryName']
        if country.endswith('a') and country not in countryset:
            countryset.add(country)
            count += 1
    print(f"Number of countries ending with 'a': {count}")
    return count

count_countries_ending_with_a(dictionary)

#-------------------------------------------------------------------------------------------------------------

#B. List the five cities that have the highest City population
def cityPop(dictionary):
    cityPopulation = []  # List to store unique city populations
    city_population_map = {}  # Dictionary to map city names to their populations

    for entry in dictionary:
        population = entry['CityPopulation']
        city = entry['CityName']

        if population is None or population == 'NULL' or population == '':
            continue
        population = int(population)  # Convert population to integer
        cityPopulation.append((population, city))
    top5 = sorted(cityPopulation, key=lambda x: x[0], reverse=True)[:5]
    
    if city not in city_population_map or population > city_population_map[city]:
            city_population_map[city] = population

    # Convert to list of (population, city) tuples
    cityPopulation = [(pop, city) for city, pop in city_population_map.items()]
    top5 = sorted(cityPopulation, reverse=True)[:5]
    
    
    print("Top 5 Cities by Population:")
    for population, city in top5:
        print(f"{city}: {population}")

    return top5

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#C List the five countries that have the largest LandMass. JESSIE/THANDO
def LandMass(dictionary):
    landMass = []  # List to store unique land masses
    count = 0

    for entry in dictionary:
        land_mass = entry['LandMass']

        if land_mass is None or land_mass == 'NULL' or land_mass == '':
            continue
        landMass.append(land_mass)
    top5 = sorted(landMass, reverse=True)[:5]
    print(top5)
    return count

#LandMass(dictionary)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#D. How many countries gained independence between the years 1960 and 1980?
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

count_countries_independent(dictionary)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#E. Which countries gained independence between the years 1830 and 1850 (inclusive)?
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
    print(f"Number of countries that gained independence between 1830 and 1850: {yearcount}")
    return yearcount

name_countries_independent(dictionary)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#F List the five African countries that have the highest life expectancy.
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

top(dictionary)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#G Which are the 5 most commonly spoken languages in the world?
def lang(dictionary):
    langlist = {}  # Set to store unique country names
    count = 0

    for entry in dictionary:
        language = entry['Language']

        langlist[language] = langlist.get(language, 0) + 1

    # Sort by count in descending order and get top 5
    top5 = sorted(langlist.items(), key=lambda item: item[1], reverse=True)[:5]

    # Print top 5
    for lang, count in top5:
        print(f"Language: {lang}, Count: {count}")

    return top5
lang(dictionary)

#-------------------------------------------------------------------------------------------------------------

#H. List the country names that end with the letter ‘a’, without any repetitions
def count_countries_ending_with_a(dictionary):
    countryset = set()  # Set to store unique country names
    count = 0

    for entry in dictionary:
        country = entry['CountryName']
        if country.endswith('a') and country not in countryset:
            countryset.add(country)

    print(countryset)
    return list(countryset)

count_countries_ending_with_a(dictionary)

#-------------------------------------------------------------------------------------------------------------

