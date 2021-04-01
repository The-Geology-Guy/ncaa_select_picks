# March Madness Bracket Picks Generator
# Project Created, Maintained, and Owned by Luke Pajer.
# For issues with file: luke.pajer@gmail.com

# Last modified: April 1st, 2021

########### SECTION 1: Import Required Packages ###########

# Import required Packages to use the predictor.

# Import numpy
import numpy as np

# Import random
import random as rd

# Import display and Mardown to show the results
from IPython.display import display, Markdown

# ---------------------------------------------------------

### SECTION 2: Function to select winner in each matchup ##

def pick_best(high_seed, low_seed):
    
    '''pick_best takes the high seed and the low seed and determines which 
    seed wins the round. The trial length is determined by the sum of the two seeds.'''
    
    # Flip the coin a number of times equal to the sum of the low and high seeds
    results = []
    trial = 0
    while trial < (low_seed + high_seed):
        coin = rd.randint(1, 2)
        if coin == 1:
            results.append('H')
            trial += 1
        elif coin == 2:
            results.append('T')
            trial += 1
    
    # Determine the winner based on the results list
    if results.count('H') > min(high_seed, low_seed):
        return high_seed
    else:
        return low_seed
    
# ---------------------------------------------------------
    
######### SECTION 3: Determine winners of Round 1 #########

def round_1():
    
    '''round_1 is a function that initiates the seeding pairs by implementing a 
    range of numbers between 1 and 16. Then, it zips together the high and low
    seeds together into a tuple. Lastly, this runs the pick_best function and 
    returns a list of the winners of the round.'''
    
    #Initiate the seed pairings for the conference (1 through 16)
    high_points = np.arange(1, 9)
    low_points = np.arange(16, 8, -1)
    
    # Zip together the high and low points and save to the variable matchups as a tuple
    matchups = tuple(zip(high_points, low_points))
    
    # Pick the winners of each matchup by looping through the matchups with the pick_best function
    results_rd = []
    i = 0
    while i < len(matchups):
        winner = pick_best(matchups[i][0], matchups[i][1])
        results_rd.append(winner)
        i += 1
        
    # Determine the halfway point of the list and only return the winning values
    halfway = int(len(results_rd) / 2)
    round_1_winners = tuple(zip(results_rd[:halfway], reversed(results_rd[halfway:])))
    return round_1_winners

# ---------------------------------------------------------

######### SECTION 4: Determine winners of Round 2 #########

def round_2(match_list):
    
    '''This runs the pick_best function for the matchups determined
    from the previous round (round_1) and returns a list of the 
    winners of the round.'''
    
    # Pick the winners of each matchup by looping through the matchups with the pick_best function
    matchups = match_list
    results_rd = []
    i = 0
    while i < len(matchups):
        winner = pick_best(matchups[i][0], matchups[i][1])
        results_rd.append(winner)
        i += 1
        
    # Determine the halfway point of the list and only return the winning values
    halfway = int(len(results_rd) / 2)
    round_2_winners = tuple(zip(results_rd[:halfway], reversed(results_rd[halfway:])))
    return round_2_winners

# ---------------------------------------------------------

######### SECTION 5: Determine winners of Sweet 16 ########

def sweet_16(match_list):
    
    '''Tthis runs the pick_best function for the matchups determined
    from the previous round (round_2) and returns a list of the 
    winners of the round.'''
    
    # Pick the winners of each matchup by looping through the matchups with the pick_best function
    matchups = match_list
    results_rd = []
    i = 0
    while i < len(matchups):
        winner = pick_best(matchups[i][0], matchups[i][1])
        results_rd.append(winner)
        i += 1
    
    # This puts the results into a list called sweet_16_winners
    sweet_16_winners = list(results_rd)
    return sweet_16_winners

# ---------------------------------------------------------

######### SECTION 6: Determine winners of Elite 8 #########

def elite_8(match_list):
    
    '''This function applies the pick_best function to the
    winners of the sweet 16 round.'''
    
    matchups = match_list
    
    # Applt the function to the matchup in the elite 8
    elite_winner = pick_best(matchups[0], matchups[1])
    return elite_winner

# ---------------------------------------------------------

######## SECTION 7: Determine winners of Final Four #######

def final_4(match_list, region_name):
    
    '''This runs the pick_final function for the matchups determined
    from the previous round (elite_8) and returns a list of the 
    winners of the round. The regions are now being used in this function
    to keep the regions and seedings together.'''
    
    matchups = tuple(zip(region_name, match_list))
    results_rd = []
    i = 0
    j = 1
    
    # The regions list ['EAST', 'WEST', 'SOUTH', 'MIDWEST']
    while i < len(matchups):
        winner = pick_final(matchups[i][1], matchups[j][1], list((matchups[i][0], matchups[j][0])))
        results_rd.append(winner)
        i += 2
        j += 2
    
    # List out the winners of the final four
    final_4_winners = list(results_rd)
    return final_4_winners

def pick_final(high_seed, low_seed, region_name):
        
    '''pick_final takes the high seed and the low seed and determines which 
    seed wins the round. The trial length is determined by the sum of the two seeds.
    The region may be South, East, Midwest, or West.'''
    
    # Flip the coin a number of times equal to the sum of the low and high seeds
    results = []
    trial = 0
    while trial < (low_seed + high_seed):
        coin = rd.randint(1, 2)
        if coin == 1:
            results.append('H')
            trial += 1
        elif coin == 2:
            results.append('T')
            trial += 1
    
    # Determine the winner based on the results list, with the winner's region included
    if results.count('H') > min(high_seed, low_seed):
        return region_name[0], high_seed
    else:
        return region_name[1], low_seed
    
# ---------------------------------------------------------
    
####### SECTION 8: Overall function to pick bracket #######

def pick_brackets(region_names):
    
    '''Combines all of the functions to produce a prediction. Be sure
    to enter the region names in a way that looks correct on the NCAA
    march madness bracket. Example: [Upper Left, Lower Left, Upper Right, Lower Right]
    would be ['EAST', 'WEST', 'SOUTH', 'MIDWEST'] in 2019.'''
    
    # The name may change depending on year, the order of the list 'name' is important
    region = []
    name = region_names
    round_ = 0
    final_four = []
    
    # Run through each of the regions and display the results
    while round_ < len(name):
        
        display(Markdown("### " + name[round_]))
        
        rd_1_group = round_1()
        display(Markdown("First Round: " + str(rd_1_group)))
        
        rd_2_group = round_2(rd_1_group)
        display(Markdown("Second Round: " + str(rd_2_group)))
        
        rd_3_group = sweet_16(rd_2_group)
        display(Markdown("Regional Semifinals: " + str(rd_3_group)))
        
        conference_winner = elite_8(rd_3_group)
        display(Markdown("Regional Finals:   " + str(conference_winner)))
        
        final_four.append(conference_winner)
        round_ += 1
        
    # Display the Winners of the National Semifinals - also known as the Final Four
    display(Markdown("### National Semifinals"))
    final_4_winners = final_4(final_four, name)
    display(Markdown(str(final_4_winners[0][0]) + ": " + str(final_4_winners[0][1])))
    display(Markdown(str(final_4_winners[1][0]) + ": " + str(final_4_winners[1][1])))
    
    # Crown the champion and display both the region and seed of the winner
    champion = pick_final(final_4_winners[0][1], final_4_winners[1][1], list((final_4_winners[0][0], final_4_winners[1][0])))
    display(Markdown("### Champion: " + str(champion[0]) + ", Seed " + str(champion[1])))