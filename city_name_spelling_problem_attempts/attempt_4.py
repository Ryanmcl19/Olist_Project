# This was my final attempt using this type of approach before realizing that I would not be able to come up with a satisfactory result regardless of the amount of refining done

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

# 1. create the empty list and dictionary
correct_spelling_list = [] # stores city, state tuples
city_name_corrections = {} # stores incorrectly spelled names along with their correction

# iterate through city counts csv
for city_spelling, state_abbv, frequency in zip(city_counts['normalized_geo_city'], city_counts['geo_state'], city_counts['frequency']):
    match_detected = False

    # create a for loop that first checks if the state abbv matches, then checks city spelling with leventshein distance
    for ((correct_spelling, correct_state), standard_frequency) in correct_spelling_list:
        # First filter: leventshein distance varies depending on city name length
        if state_abbv == correct_state:
            leventshein_distance = jellyfish.levenshtein_distance(city_spelling, correct_spelling)
            if len(city_spelling) <= 12 or len(correct_spelling) <= 12:
                    allowed_distance = 1
            else:
                allowed_distance = 2
            # Second filter: the frequency of the already-verified spelling must also be at least 10x more common than the
            # spelling that is actively being checked. This helps distinguish populated cities that share near-identical spellings
            # with other populated cities
            is_rare_typo = (standard_frequency / frequency) >= 15 if frequency > 0 else True

            # Third filter: if the first letters do not match, odds are that its not a typo and instead a new city name.
            first_letters_match = city_spelling[0] == correct_spelling[0]

            if leventshein_distance <= allowed_distance and is_rare_typo and first_letters_match:
                match_detected = True
                # Store the correction using a unique key (city + state)
                city_name_corrections.update({
                    f"{city_spelling}|{state_abbv}": correct_spelling
                })
                break

    # if the city, state pair has not been detected, add it to the list as a new correct spelling
    if not match_detected:
        correct_spelling_list.append(((city_spelling, state_abbv), frequency))

print(f"Original unique city spellings & state combinations: {len(city_counts)}")
print(f"New 'Standard' city spellings & state combinations: {len(correct_spelling_list)}")
print(f"Number of typos identified: {len(city_name_corrections)}")
