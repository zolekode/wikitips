import requests
import urllib.parse
import logging
import xmltodict
from collections import OrderedDict


class DBPClueExtractor:
    __URL = "http://lookup.dbpedia.org/api/search/{}?QueryClass={}&QueryString={}&MaxHits={}"

    __KEYWORD_SEARCH = 0
    __PREFIX_SEARCH = 1

    __QUERY_PARAMS = {
        __KEYWORD_SEARCH: "KeywordSearch",
        __PREFIX_SEARCH: "PrefixSearch",
    }

    __ARRAY_OF_RESULTS = "ArrayOfResult"
    __RESULT = "Result"
    __LABEL = "Label"
    __DESCRIPTION = "Description"
    __CLASSES = "Classes"
    __CATEGORIES = "Categories"
    __CLASS = "Class"
    __CATEGORY = "Category"

    def get_keyword_clues(self, keyword: str, dbpedia_class: str = "", limit: int = 1) -> list:
        """
        :param keyword: The string you want to search. Note that special chars will be encoded.
        :param dbpedia_class: The dbpedia class as in: http://mappings.dbpedia.org/server/ontology/classes/
        :param limit: The max number of elements in your results. Keep this value as small as possible.
        :return: The clues as a list of dicts
        """
        return self.__handle_requests(keyword, dbpedia_class, limit, self.__QUERY_PARAMS[self.__KEYWORD_SEARCH])

    def get_prefix_clues(self, prefix: str, dbpedia_class: str = "", limit: int = 1) -> list:
        """
        :param prefix: The prefix string
        :param dbpedia_class: The dbpedia class as in: http://mappings.dbpedia.org/server/ontology/classes/
        :param limit: The max number of elements in your results. Keep this value as small as possible.
        :return: The clues as a list of dicts
        """
        return self.__handle_requests(prefix, dbpedia_class, limit, self.__QUERY_PARAMS[self.__PREFIX_SEARCH])

    def __handle_requests(self, keyword: str, dbpedia_class: str, limit: int, query_type: str) -> list:
        if not isinstance(keyword, str) or len(keyword) == 0:
            raise Exception("Keyword must be a non empty string. For example keyword=\"Python\"")

        keyword = urllib.parse.quote(keyword, safe="")
        url = self.__URL.format(query_type, dbpedia_class, keyword, limit)

        try:
            response = requests.get(url=url)
        except requests.exceptions.RequestException as e:
            logging.error("An error occurred. Retry again later or use different parameters.")
            return list()

        content = xmltodict.parse(response.content)
        return self.__extract_information_from_content(content)

    def __extract_information_from_content(self, content: OrderedDict) -> list:
        information = content[self.__ARRAY_OF_RESULTS]
        if self.__RESULT not in information:
            return list()
        information = information[self.__RESULT]
        if not isinstance(information, list):
            information = [information]

        return self.__extract_information_from_dictionary_objects(information)

    def __extract_information_from_dictionary_objects(self, dictionary_objects: list) -> list:
        results = list()
        for dict_object in dictionary_objects:
            results.append(self.__extract_information_from_dictionary(dict_object))
        return results

    def __extract_information_from_dictionary(self, dictionary: OrderedDict) -> dict:
        result = dict()
        result[self.__LABEL] = self.__get_value(dictionary, self.__LABEL)
        result[self.__DESCRIPTION] = self.__get_value(dictionary, self.__DESCRIPTION)
        result[self.__CLASSES] = self.__get_classes(dictionary)
        result[self.__CATEGORIES] = self.__get_categories(dictionary)

        return result

    def __get_value(self, dictionary, key: str) -> str:
        if key in dictionary:
            return dictionary[key]
        return ""

    def __get_classes(self, dictionary: OrderedDict) -> list:
        return self.__get_values_from_objects(dictionary, self.__CLASSES, self.__CLASS)

    def __get_categories(self, dictionary: OrderedDict) -> list:
        return self.__get_values_from_objects(dictionary, self.__CATEGORIES, self.__CATEGORY)

    def __get_values_from_objects(self, dictionary, super_key: str, sub_key: str) -> list:
        if super_key in dictionary:
            classes = list()
            if sub_key in dictionary[super_key]:
                classes = dictionary[super_key][sub_key]
                if not isinstance(classes, list) and isinstance(classes, OrderedDict):
                    classes = [classes]
            return self.__extract_classes_from_list(classes)
        return list()

    def __extract_classes_from_list(self, classes: list) -> list:
        results = list()
        for class_object in classes:
            results.append(self.__get_value(class_object, self.__LABEL))
        return results
