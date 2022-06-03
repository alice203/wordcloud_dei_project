# wordcloud_dei_project

This project is about an exploratory data analysis for the voluntary DEI (diversity, equality & inclusion) team at my employer.

The goal was to assess and understand the perception of diversity & inclusion and status quo in the company. One part of this audit was to understand how diverse and inclusive our products are. For this, I reviewed the characters of our flagship games and their descriptions to understand:

* The overall representation of genders* within our games
* Whether specific words are used to describe the characters by gender

**It is important to state that diversity and inclusion goes beyond gender. However, given the nature of the characters in the game, gender seemed like a feasible and good first feature to analyse

## Findings

* Even though [55% of of mobile gamers in the US are women](https://www.statista.com/statistics/1243409/us-mobile-gaming-users-gender/), one of our games has less than 25% female representation in game characters, and 17% neutral character representation. 

![props](https://github.com/alice203/wordcloud_dei_project/blob/main/plots/props.png?raw=true)

* Words, and especially adjectives, used for describing different characters seem at first glance evenly among gender when looking at positive & negative adjectives. Prominent words for all genders are **cosmic**, **dangerous**, **good**, **powerful**, **dark**

* When removing shared adjectives and displaying remaining adjectives that are most common by genders, characters are indeed described with stereotypical adjectives for genders. E.g. male characters are described as **tough**, **legendary** and **aggressive**, whereas female characters are described as **desperate**, **beautiful** and **fairy**

![male](https://github.com/alice203/wordcloud_dei_project/blob/main/plots/wc4_mark.png?raw=true)

![female](https://github.com/alice203/wordcloud_dei_project/blob/main/plots/wc5_mark.png?raw=true)
