# names of hurricanes
from calendar import c


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

# write your update damages function here:
def updated_damages(damages):
    updated_damages = []
    for case in damages:
        if(case[-1]=='M'):
            updated_case = float(case[:-1])*10**6
            updated_damages.append(updated_case)
        elif(case[-1]=='B'):
            updated_case = float(case[:-1])*10**9
            updated_damages.append(updated_case)
        else:
            updated_damages.append(case)
    return updated_damages

updated_damages = updated_damages(damages)             
#print(updated_damages)

# write your construct hurricane dictionary function here:
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
       hurricanes = {}
       for i in range(len(names)):
            hurricanes.update({names[i]:
            {
            "Name": names[i], 
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i], 
            "Damage": updated_damages[i], 
            "Deaths": deaths[i]
            }
        })
       return hurricanes

hurricanes = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)

# write your construct hurricane by year dictionary function here:
def hurricane_by_year(hurricanes):
    hurricanes_by_year = {}
    for cane in hurricanes:
        current_year = hurricanes[cane]["Year"]
        if(current_year not in hurricanes_by_year):
            hurricanes_by_year.update({current_year:hurricanes[cane]})
    return hurricanes_by_year

hurricanes_by_year = hurricane_by_year(hurricanes)
#print(hurricanes_by_year)


# write your count affected areas function here:

def cane_frequency(hurricanes):
    cane_frequency = {}
    cane_count = 1
    for cane in hurricanes:
        for area in tuple(hurricanes[cane]["Areas Affected"]):
        #print(area)
            if(area in cane_frequency):
                cane_count +=1
                cane_frequency.update({area:cane_count})

            else:
                cane_frequency.update({area:1})
        
    return cane_frequency

hurricane_frequency = cane_frequency(hurricanes)
#print(hurricane_frequency)

# write your find most affected area function here:
def most_affected_area(hurricane_frequency):
    current_area = ['']
    current_cane_count = 0
    for area in hurricane_frequency:
        if hurricane_frequency[area] > current_cane_count:
            current_cane_count = hurricane_frequency[area]
            current_area[0] = area
        elif hurricane_frequency[area] < current_cane_count:
            continue
        elif hurricane_frequency[area] == current_cane_count:
            current_area.append(area)
    return current_area, current_cane_count
            
most_affected_area = most_affected_area(hurricane_frequency)
#print(most_affected_area)

# write your greatest number of deaths function here:
def highest_cane_mortality(hurricanes):
    current_death_count = 0
    current_cane=['']
    for cane in hurricanes:
        death_count = hurricanes[cane]["Deaths"]
        if death_count > current_death_count:
            current_death_count = death_count
            current_cane[0] = cane
        elif death_count < current_death_count:
            continue
        elif death_count == current_death_count:
            current_cane.append(cane)
    return current_cane, current_death_count

highest_cane_mortality = highest_cane_mortality(hurricanes)
#print(highest_cane_mortality)


# write your catgeorize by mortality function here:

def mortality_scale(hurricanes):
    mortality_rating = {0:[],
                        1: [],
                        2:[],
                        3: [],
                        4:[]}
    mortality_scale = {0: 0,
                        1:100,
                        2:500,
                        3:1000,
                        4:10000}
    
    for cane in hurricanes:
        current_cane = hurricanes[cane]["Deaths"]
        if current_cane == 0:
            #new_dict = mortality_rating.update({0:cane})
            mortality_rating[0].append(cane)
        elif current_cane > 0 and current_cane <= 100:
            #new_dict = mortality_rating.update({1:cane})
            mortality_rating[1].append(cane)
        elif current_cane >100 and current_cane <= 500:
            #new_dict = mortality_rating.update({2:cane})
            mortality_rating[2].append(cane)
        elif current_cane >500 and current_cane <= 1000:
            #new_dict = mortality_rating.update({3:cane})
            mortality_rating[3].append(cane)
        elif current_cane >1000 and current_cane <= 10000:
            #new_dict = mortality_rating.update({4:cane})
            mortality_rating[4].append(cane)
    return mortality_rating

cane_by_mortality_rating = mortality_scale(hurricanes)
#print(cane_by_mortality_rating)


# write your greatest damage function here:
def cane_greatest_damage(hurricanes):
    current_cane_cost = 0
    current_cane = []
    for cane in hurricanes:
        current_damage = hurricanes[cane]["Damage"]
        if type(current_damage) == str:
            continue
        elif current_damage > current_cane_cost:
            current_cane_cost = hurricanes[cane]["Damage"]
            current_cane = [cane, current_cane_cost]
    return current_cane

costliest_cane = cane_greatest_damage(hurricanes)
#print(costliest_cane)


# write your catgeorize by damage function here:
def cane_by_damage(hurricanes):
    damage_scale = {0:0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000,
                    5: 'Damages not recorded'}

    cane_by_damage = {0:[],
                    1: [],
                    2: [],
                    3: [],
                    4:[],
                    5: [],
                    'Damages not recorded': []}
    for cane in hurricanes:
        current_damage = hurricanes[cane]["Damage"]
        if type(current_damage) == str:
            cane_by_damage['Damages not recorded'].append(cane)
        elif current_damage > 0 and current_damage <= 100000000:
            cane_by_damage[1].append(cane)
        elif current_damage > 100000000 and current_damage <= 1000000000:
            cane_by_damage[2].append(cane)
        elif current_damage > 1000000000 and current_damage <= 10000000000:
            cane_by_damage[3].append(cane)
        elif current_damage > 10000000000 and current_damage <= 500000000000:
            cane_by_damage[4].append(cane)
        elif current_damage > 500000000000:
            cane_by_damage[5].append(cane)
    return cane_by_damage

cane_by_damage = cane_by_damage(hurricanes)
print(cane_by_damage)
