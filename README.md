<img src="wikitips.png"/>
# Wikitips
WikiTips is a very simple to use library that extracts semantic clues from DBPedia (The knowledge base system built from Wikipedia's data).

Currently there is no pip package so just go ahead and clone or download it into your own projects.

# Usage
There are two functions you can call to get wikitips: 

`get_keyword_clues(prefix:str, dbpedia_class:str, limit:int)` and `get_prefix_clues(prefix:str, dbpedia_class:str, limit:int)`

* The first function takes a keyword as argument. A key word might have multiple tokens. The second function takes in a word prefix (searches for objects that have a name or label starting with the prefix). 

* `dbpedia_class` an optional attribute. Allowed values correspond to the DBPedias's ontology classes found here: http://mappings.dbpedia.org/server/ontology/classes/. The default value is an empty string. Use this attribute only if you know about ontology classes. If you don't you would probably still end up fine :). 

* `limit` is also optional. That is just the maximum number of hits or objects returned. The default value is **1**.


**Example 1**

```
from core.clue_extraction import DBPClueExtractor

sample_keyword = "Japan"

dbp_clue_extractor = DBPClueExtractor()
wiki_tips = dbp_clue_extractor.get_keyword_clues(sample_keyword)
print(wiki_tips)
```

**Results**:

```
[
   {
      "Label":"Japan",
      "Description":"Japan Listen/dʒəˈpæn/ (Japanese: 日本 Nihon or Nippon; formally 日本国 or Nihon-koku, literally the State          of Japan) is an island nation in East Asia. Located in the Pacific Ocean, it lies to the east of the Sea of Japan,            China, North Korea, South Korea and Russia, stretching from the Sea of Okhotsk in the north to the East China Sea and          Taiwan in the south. The characters that make up Japan\\'s name mean \"sun-origin\", which is why Japan is sometimes          referred to as the \"Land of the Rising Sun\".",
      "Classes":[
         "country",
         "populated place",
         "place",
         "country",
         "owl#Thing",
         "place"
      ],
      "Categories":[
         "Countries bordering the Philippine Sea",
         "Liberal democracies",
         "Constitutional monarchies",
         "States and territories established in 660 BC",
         "G8 nations",
         "Member states of the United Nations",
         "East Asian countries",
         "Countries bordering the Pacific Ocean",
         "Island countries",
         "G20 nations",
         "Japan",
         "Empires"
      ]
   }
]
```

**Example 2**

```
sample_keywords = "New York"

dbp_clue_extractor = DBPClueExtractor()
wiki_tips = dbp_clue_extractor.get_keyword_clues(sample_keywords, dbpedia_class="City")
print(wiki_tips)
```

**Results**

```
[
   {
      "Label":"New York City",
      "Description":"New York is the most populous city in the United States and the center of the New York Metropolitan Area,        one of the most populous metropolitan areas in the world. The city is referred to as New York City or The City of New          York to distinguish it from the State of New York, of which it is a part. As a global power city, New York exerts a            significant impact upon commerce, finance, media, art, fashion, research, technology, education, and entertainment.",
      "Classes":[
         "city",
         "populated place",
         "settlement",
         "place",
         "owl#Thing",
         "place",
         "city"
      ],
      "Categories":[
         "Government of New York City",
         "Populated places established in 1624",
         "Populated places on the Hudson River",
         "Former United States state capitals",
         "Cities in New York",
         "Port settlements in the United States",
         "New York City",
         "Metropolitan areas of the United States",
         "1624 establishments in the Thirteen Colonies",
         "Former capitals of the United States"
      ]
   }
]
```
**Example 3**
```
sample_prefix = "Foot"

dbp_clue_extractor = DBPClueExtractor()
wiki_tips = dbp_clue_extractor.get_prefix_clues(sample_prefix, dbpedia_class="Sport", limit=1)
print(wiki_tips)
```

**Results**

```
[
   {
      "Label":"Association football",
      "Description":"Association football, more commonly known as football or soccer, is a sport played between two teams of          eleven players with a spherical ball. At the turn of the 21st century, the game was played by over 250 million players        in over 200 countries, making it the world's most popular sport. The game is played on a rectangular field of grass or        green artificial turf, with a goal in the middle of each of the short ends. The object of the game is to score by              driving the ball into the opposing goal.",
      "Classes":[
         "sport",
         "owl#Thing",
         "activity"
      ],
      "Categories":[
         "Laws of association football",
         "Football codes",
         "Association football",
         "Association football terminology",
         "Ball games",
         "Sports originating in England"
      ]
   }
]
``` 

You can now enrich your NLP pipelines with Semi-Structured data. Have fun mining.
