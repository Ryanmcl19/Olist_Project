# Olist_Project
I've downloaded the Olist Ecommerce dataset from Kaggle in order to further develop my skills in data cleaning, data analysis, and data visualization using Tableau


## Challenges and Solutions
One of the key points in the decision-making process was in deciding what method to use for organizing and merging all the various spellings of city names in the geolocation, customers, and sellers datasets.
Applying the pre-cleaning for the standardized city name columns helped decrease the leventshein distance between one spelling of a city to the other, on average, while still easily being able to infer the intended city. 
### 

Issues: the merging of cities such as ibia and ibiuna, itapeva and itapevi, cities with the same name but in different states, and any cities with short names (len < 5). all of these can be addressed. however, the one issue that cannot be solved is that district names, neighborhoods, post office branches, and delivery hubs. /n

So why didn't I just stick to state-level analytics where all of these issues no longer affect the data cleaning process?
1. The business wouldn't learn much that isn't already common sense. For example, the data would show sao paulo as the state contributing the most amount of sales.
2. City-level analytics, even with it's inherent issues, would still provide more actionable data at a mcuh higher level of integrity by preserving the geographical accuracy of each location. 
