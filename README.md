# Wikitips
WikiTips is a very simple to use library that extracts semantic clues from DBPedia (The knowledge base system built from Wikipedia's data).

Currently there is no pip package so just go ahead and clone or download it into your own projects.

# Usage
```
from core.clue_extraction import DBPClueExtractor

sample_keyword = "Japan"

dbp_clue_extractor = DBPClueExtractor()
wiki_tips = dbp_clue_extractor.get_keyword_clues(sample_keyword)
print(wiki_tips)
```

If you run that code, you will get this:

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
