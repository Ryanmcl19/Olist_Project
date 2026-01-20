# This is one of the conservative attempts made but resulted in 5979 new standard spellings and only 337 typos found, out of 6316 unique spellings, while immediately seeing city names that shouldnt have been merged together.


import pandas as pd
import csv
import jellyfish


city_counts = pd.read_csv("C:\SQL_projects\Olist\datasets\olist_city_counts.csv",
        dtype={
            'normalized_geo_city' : str,
            'frequency' : int,
            'normalized_pct' : float
        }
)

# test x, leventshein distance, at 2 and 1 and see how the results come out.
# create a list that unique city names only
# \. this list will be referred to when measuring the leventshein
# distance to the other spellings. if their spelling is within x distance from spelling in the index of list, y, change
# the spelling to list[y]

# 1. create the empty list and dictionary
correct_spelling_list = [] # stores city, state tuples
city_name_corrections = {} # stores incorrectly spelled names along with their correction

# iterate through city counts csv
for city_spelling, state_abbv in zip(city_counts['normalized_geo_city'], city_counts['geo_state']):
    match_detected = False

    # create a for loop that first checks if the state abbv matches, then checks city spelling with leventshein distance
    for correct_spelling, correct_state in correct_spelling_list:

        if state_abbv == correct_state:
            leventshein_distance = jellyfish.levenshtein_distance(city_spelling, correct_spelling)
            if len(city_spelling) <= 5 or len(correct_spelling) <= 5:
                    allowed_distance = 1
            else:
                allowed_distance = 2
            if leventshein_distance <= allowed_distance:
                match_detected = True
                # Store the correction using a unique key (city + state)
                city_name_corrections.update({
                    f"{city_spelling}|{state_abbv}": correct_spelling
                })
                break

    # if the city, state pair has not been detected, add it to the list as a new correct spelling
    if not match_detected:
        correct_spelling_list.append((city_spelling, state_abbv))

print(f"Original unique spellings: {len(city_counts)}")
print(f"New 'Standard' spellings: {len(correct_spelling_list)}")
print(f"Number of typos identified: {len(city_name_corrections)}")
