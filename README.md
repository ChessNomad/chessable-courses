# Source:

Creator/Donor: 
David Miedema

Source:
[Chessable.com](chessable.com)

# Data Set Information:
One of the most interesting platforms to interactively learn chess is [chessable](chessable.com). The platform offers courses where learners get direct feedback on what they are doing. This can be textual feedback or even video. 

The platform has recently been bought by chess world champion Magnus Carlsen to support the ongoing quest to digitalize and professionalize chess. At 30-07-2020 there are a total of 380 courses and bundles available on chessable. From now on I will use the word course when I use course or bundle. 

The details of all these courses were scraped using Selenium, the scraping script is included. 

# Attribute Information:
There are 23 relevant columns
1: **course_link**
2: **course_title**
3: **course_type** -- This field specifies about which field the course is about. Opening, Tactics, Strategy, Endgame or a combination. There is also a bundle option.
4: **author** -- The author of the course, which can be a real name or an alias. This field also includes their chess titles: NM, CM, FM, IM, GM and women titles with a W in front of it.
5: **price** -- Course price in €.
6: **price_with_video** -- Price in € for additional video material. Contains missing values.
7: **course_rating** -- Ratings based on a five star system.
8: **course_rating_count** -- The amount of ratings per course.
9: **rubies** -- The amount of rubies donated to a course. One Ruby = $0.05
10: **target_color** -- The color at which the course is aimed: black, white or both.
11: **beginning** -- The following five columns represent the target audience rating: ELO 800 - 1000
12: **casual** -- ELO 1000 - 1400
13: **intermediate** -- ELO 1400 - 1800
14: **advanced** -- ELO 1800 - 2100
15: **expert** -- ELO 2000 - 2400
16: **language** 
17: **instruction_word_count** -- The amount of feedback in words per course.
18: **free_video** -- The duration of free video available.
19: **trainable_variations** -- The amount of variations with feedback-training.
20: **avg_line_depth** -- The average amount of moves per variation.
21: **released_on** -- The releasedate of the course.
22: **support_level**
23: **section** -- This field describes the nature of the contributor: Titled player, Community or Publisher.
