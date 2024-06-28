# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages

def func1(list):
    new_list = []

    for x in damages:
        if x == "Damages not recorded":
            new_list.append(x)
        else:
            multiplier = x[-1]
            if x[:-1].replace('.', '', 1).isdigit():  # Check if the value is a valid number
                value = float(x[:-1])
                new_list.append(value * conversion[multiplier])

    return new_list
# here i save the updated and corrected damages list
new_damages = func1(damages)
max_damages = func1(damages)



# 2 
# Create a Table
# Create and view the hurricanes dictionary

hurr_dict = {}
for names, months, years, max_sustained_winds, areas_affected, new_damages, deaths in zip(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths):
  hurr_dict[names] =  [names, months, years, max_sustained_winds, areas_affected, new_damages, deaths]
#print(hurr_dict)


# 3
# Organizing by Year

year_dict = {}
for names, months, years, max_sustained_winds, areas_affected, damages, deaths in zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  year_dict[years] =  [names, months, years, max_sustained_winds, areas_affected, damages, deaths]
print(year_dict)


# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in

new_areas_affected = []
areas_count = []
count = 0
for x in areas_affected:
  new_areas_affected.extend(x)

dist_areas_list = list(set(new_areas_affected))
"""
"""
print(dist_areas_list)
print("==================================================================")
print(new_areas_affected)



for x in dist_areas_list:
  count = 0
  for y in new_areas_affected:
    if y == x:
      #print(x)
      count+=1
  areas_count.append(count)


counting_damaged_areas = {}
for dist_areas_list, areas_count in zip(dist_areas_list, areas_count):
  counting_damaged_areas[dist_areas_list] = areas_count
#print(counting_damaged_areas)

# 5 
# Calculating Maximum Hurricane Count

max_area = ""
helping_list = list(counting_damaged_areas.items())
max_number = helping_list[0][1]
#print(max_number)
for name, number in counting_damaged_areas.items():
  if number > max_number:
    max_number = number
    max_area = name
#print("The most affected area is : "+ max_area+ " with a total number of hurricanes : "+ str(max_number))


  

# 6
# Calculating the Deadliest Hurricane



# find most frequently affected area and the number of hurricanes involved in
max = 0
max_name = ""
for x in range(len(deaths)):
  if deaths[x]>max:
    max = deaths[x]
    max_name = names[x]
print(max)
print(max_name)





# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality

my_deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

mortality_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}

for key, value in hurr_dict.items():
  #if value['deaths'] > 0 and value['deaths'] < 100:
  #i want to insert hurr_dict[x] into mortality_dict
  if value[6] > 0 and value[6] < 100:
    mortality_dict[0].append(hurr_dict[key])

  elif value[6] > 100 and value[6]< 500:
    mortality_dict[1].append(hurr_dict[key])

  elif value[6] > 500 and value[6]< 1000:
    mortality_dict[2].append(hurr_dict[key])

  elif value[6] > 1000 and value[6]< 10000:
    mortality_dict[3].append(hurr_dict[key])

  elif value[6] > 10000:
    mortality_dict[4].append(hurr_dict[key])



    



# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

#The updated table for damages is the max_damages from step 1
#print(max_damages)
def hurricanes():
  max = 0
  for x in max_damages:
    if x != "Damages not recorded":
      if x > max:
        max = x
  return max



# find highest damage inducing hurricane and its total cost

max_damage = hurricanes()
for key, value in hurr_dict.items():
  if value[5] == max_damage:
    print("The greatest hurricane was " + key + "with a total damage with cost " + str(value[5]))



# 9
# Rating Hurricanes by Damage
rating_hurr =  {0:[], 1:[], 2:[], 3:[], 4:[]}
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

for hurr, damages in hurr_dict.items():
  if damages[5] != "Damages not recorded":
    if damages[5] > damage_scale[0] and damages[5] < damage_scale[1]:
      rating_hurr[0].append(hurr_dict[hurr])
    elif damages[5] > damage_scale[1] and damages[5] < damage_scale[2]:
      rating_hurr[1].append(hurr_dict[hurr])
    elif damages[5] > damage_scale[2] and damages[5] < damage_scale[3]:
      rating_hurr[2].append(hurr_dict[hurr])
    elif damages[5] > damage_scale[3] and damages[5] < damage_scale[4]:
      rating_hurr[3].append(hurr_dict[hurr])
    elif damages[5] > damage_scale[4]:
      rating_hurr[4].append(hurr_dict[hurr])
  

print(rating_hurr)






# categorize hurricanes in new dictionary with damage severity as key
