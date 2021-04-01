# ncaa_select_picks Python Package and Jupyter Notebook.

Main Project Resources: [PAJER, Luke](mailto:luke.pajer@gmail.com)

_Last Updated: April 2021_

[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![License](https://img.shields.io/badge/LICENSE-mit-43B02A.svg)](/LICENSE)
[![jupyterlab](https://img.shields.io/badge/jupyterlab-0.35.4-F37821.svg)](https://jupyterlab.readthedocs.io/en/stable/)
[![python](https://img.shields.io/badge/python-3.6.5-yellow.svg)](https://jupyterlab.readthedocs.io/en/stable/)
[![wiki](https://img.shields.io/badge/wiki-complete-orange)](https://github.com/The-Geology-Guy/ncaa_select_picks/wiki)

# PROJECT OVERVIEW

The purpose of the ncaa_select_picks repository is two fold:

1. Provide Python package that those more experienced with Python may use to fill out NCAA Men\'s March Madness brackets who just want to fill out a bracket for fun. _Remember that this is no better than random, so this should not be used for any financial investments._
2. Provide an easy to use Python notebook for anyone to use to develop their understanding of Python and algorithms. This may be used in a classroom or at an individual level. I encourage people to adapt this to other playoff brackets of other sports!

**_Disclaimer: the package should be used for fun or research/education purposes. It should not be used for any financial investment as it is likely no better than random at predicting picks. If you or a loved one has any issues with Gambling, please contact the National Gambling hotline at 1-800-522-4700._**

If there are any issues or concerns regarding the `ncaa_select_picks` package or notebook, please reach out to [Luke Pajer](mailto:luke.pajer@gmail.com).

## CONTRIBUTORS

This project is an open project, and contributions are welcome from any individual. All contributors to this project are bound by a [code of conduct](/CODE_OF_CONDUCT.md). Please review and follow this code of conduct as part of your contribution.

#### Contributions to the ncaa_select_picks Python Package
- [Luke Pajer](mailto:luke.pajer@gmail.com) [![orcid](https://img.shields.io/badge/orcid-0000--0002--5218--7650-brightgreen.svg)](https://orcid.org/0000-0002-5218-7650)

#### Contributions to the ncaa_select_picks Python Notebook
- [Luke Pajer](mailto:luke.pajer@gmail.com) [![orcid](https://img.shields.io/badge/orcid-0000--0002--5218--7650-brightgreen.svg)](https://orcid.org/0000-0002-5218-7650)

### Tips for Contributing

Issues and bug reports are always welcome.  Code clean-up, and feature additions can be done either through pull requests to [project forks]() or branches.

All products of the SLAM project are licensed under an [MIT License](LICENSE) unless otherwise noted.

-----

# Install Python Package

```pip install ncaa_select_picks```

### System Requirements

This project is developed using Python. There should be no issues with these projects running on Mac, Windows, or Linux. If there are any issues, please submit an issue and it will be investigated.

-----

# Introduction to the Python Notebook

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

The rest of this notebook is available here in the repository. Please feel free to download and use the notebook for personal/education/research purposes.
