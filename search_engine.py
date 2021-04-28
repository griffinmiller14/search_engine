"""
Griffin Miller
CSE 163 AI
This program implements the SearchEngine Class for HW4.
"""
import os
import re
import math
from document import Document


class SearchEngine:
    """
    This class represents a search engine object with a file
    count and an inverted index mapping terms to documents
    containing that term.
    """
    def __init__(self, directory):
        """
        Inititializes a SearchEngine object with given file
        directory as a paramter.
        """
        self._file_count = 0
        self._inverted_index = {}
        for file_name in os.listdir(directory):
            self._file_count += 1
            path = directory + '/' + file_name
            doc = Document(path)
            for word in doc.get_words():
                if word not in self._inverted_index.keys():
                    self._inverted_index[word] = [doc]
                else:
                    self._inverted_index[word].append(doc)

    def search(self, term):
        """
        Takes in a search query as a paramter. The query is converted to
        lowercase and normalized. Returns a list of documents that contain
        at least one of the tokens in the search query. If none of the
        tokens in the query appear in any of the documents, returns None.
        Sorts the returned list by documents TF-IDF in descending order.
        """
        terms = []
        for word in term.split():
            word = re.sub(r'\W+', '', word).lower()
            terms.append(word)
        relevant_docs = set()
        for term in terms:
            if term in self._inverted_index.keys():
                for doc in self._inverted_index[term]:
                    relevant_docs.add(doc)

        if not relevant_docs:
            return None
        else:
            temp = []
            result = []
            for doc in relevant_docs:
                tf_idf_doc = 0
                for word in terms:
                    tf_word = doc.term_frequency(word)
                    idf_word = self._calculate_idf(word)
                    tf_idf_word = tf_word * idf_word
                    tf_idf_doc += tf_idf_word
                temp.append((doc.get_path(), tf_idf_doc))

            temp = sorted(temp, key=lambda d: d[1], reverse=True)
            for i in temp:
                result.append(i[0])
            return result

    def _calculate_idf(self, term):
        """
        Takes in an individual token from the search query as a paramter
        and calculates the term's inverse document frequency. If term
        doesnt appear in any documents, returns 0. The term will already be
        converted to lowercase and normalized as a paramter.
        """
        if term in self._inverted_index.keys():
            return math.log(self._file_count /
                            len(self._inverted_index[term]))
        else:
            return 0
