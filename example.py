from core.clue_extraction import DBPClueExtractor

sample_keyword = "Japan"

dbp_clue_extractor = DBPClueExtractor()
wiki_tips = dbp_clue_extractor.get_keyword_clues(sample_keyword)
print(wiki_tips)

sample_keywords = "New York"

dbp_clue_extractor = DBPClueExtractor()
wiki_tips = dbp_clue_extractor.get_keyword_clues(sample_keywords, dbpedia_class="City")
print(wiki_tips)

sample_prefix = "Foot"

dbp_clue_extractor = DBPClueExtractor()
wiki_tips = dbp_clue_extractor.get_prefix_clues(sample_prefix, dbpedia_class="Sport", limit=1)
print(wiki_tips)
