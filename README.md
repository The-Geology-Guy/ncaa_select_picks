### Introduction to the ncaa_select_picks Python Notebook

Every year, millions of people across the globe tune into the madness of the NCAA Men's Basketball tournament March Madness. This is a tournament involving 64 teams, all with the mission to win every game and be crowned the best in Men's Collegiate Basketball. 

![Show Image](https://upload.wikimedia.org/wikipedia/en/thumb/2/28/March_Madness_logo.svg/220px-March_Madness_logo.svg.png)
###### Image source: https://upload.wikimedia.org/wikipedia/en/thumb/2/28/March_Madness_logo.svg/220px-March_Madness_logo.svg.png

The madness does not just stay on the court, as millions of people each year will fill out brackets in hope that their's will be one of the well known perfect brackets. This perfect bracket is, of course, just improbable, as there are about <img src="https://latex.codecogs.com/gif.latex?1.27\times10^{89}"/> different combinations of outcomes for a 64 team bracket. Still, the infintesimal probability does not stop people from filling out multiple brackets, with the hope of having at least the best in their office!

- **Round 1:** 64 teams split into 4 regions with 16 teams in each region (_region names change year to year_)
- **Round 2:** 32 teams remain in total, split between the 4 regions with 8 teams remaining in each region
- **Regional Semifinals (Sweet 16):** 16 teams remain in total, split between the 4 regions with 4 teams remaining in each region
- **Regional Finals (Elite 8):** 8 teams remain in total, split between the 4 regions with 2 teams remaining in each region
- **National Semifinals (Final 4):** the winning team for each region go head-to-head with the opposing region, ex. EAST vs. WEST & SOUTH vs. MIDWEST
- **National Championship:** only 2 teams remain and will battle to be crowned the best basketball team in NCAA Men's Collegiate Basketball

In this notebook, we will explore a way to make predictions based on coin flips. In essence, the model takes the seeding pairs of matchups and pins them against each other in a game involving chance. 

For example, if a 5 seed were to play a 12 seed, then the following would occur:

- 17 total flips of a coin
- If there are more than 5 occurances of 'Heads' in the set of coin flips, then the **Higher** seed (5) wins.
- If there are 13 or more occurances of 'Tails' in the set of coin flips, then the **Lower** seed (12) wins.

This basic scenario will determine each match up. However, there are some other factors to be taken into account when moving forward with the tournament.

To begin this process, we will first need to import the packages we will be using throughout this predictor. The two packages to import are numpy and random.
