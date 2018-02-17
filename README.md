# 203MongoPie

<h3>work.py</h3>
Contains methods to search for:
<ul>
  <li>All restaurants in a specified borough.</li>
  <li>All restaurants in a specified zip code.</li>
  <li>All restaurants in a specified zip code and with a specified grade.</li>
  <li>All restaurants in a specified zip code with a score below a specified threshold.</li>
  <li>All restaurants by cuisine in a specified borough and with a specified grade.</li>
</ul>
<h3>db.py</h3>
NAME: United States Population Table (Ages 0-100) in 2010

DESCRIPTION: This dataset contains information about the number of females and males of each age (0 to 100) in the U.S.

DOWNLOAD HYPERLINK: http://api.population.io/1.0/population/2010/United%20States/?format=json

IMPORT MECHANISM:
1. Uses urllib2 library to open the JSON file from the link to be read.
2. .loads turns JSON object into a dictionary.
3. Creates the database "gaoJsoeW" and collection "population".
4. Inserts documents into the collection "population".  There is one document for each age; each document contains the age ("age"), number of females ("females"), number of males ("males"), and the total [females + males] ("total").
