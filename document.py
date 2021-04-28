"""
Griffin Miller
CSE 163 AI
This program implements the Document Class for HW4.
"""
import re


class Document:
    """
    Represents a document with file name, a list of words within the
    document, a mapping of each uniqe word to number of times that word
    appears, and an overall word count of the document.
    """
    def __init__(self, file_name):
        """
        Initializes a Document object with a file name passed in as
        a paramater.
        """
        self._word_to_count = {}
        self._doc = []
        self._file_name = file_name
        with open(file_name) as f:  # turn doc into list
            for word in f.read().split():
                word = re.sub(r'\W+', '', word).lower()
                self._doc.append(word)

        for word in self._doc:  # map word to count
            if word not in self._word_to_count.keys():
                self._word_to_count[word] = 1
            else:
                self._word_to_count[word] += 1

        self._word_count = 0
        for key in self._word_to_count:  # count total words in doc
            self._word_count += self._word_to_count[key]

    def term_frequency(self, term):
        """
        Takes in a term as a paramter and returns the TF of the
        given term within the document. The given term is converted to
        lowercase and stripped of punctuation. If the given term is not
        within the document, it returns 0.
        """
        term = re.sub(r'\W+', '', term).lower()
        if term not in self._word_to_count.keys():
            return 0
        else:
            return self._word_to_count[term] / self._word_count

    def get_words(self):
        """
        Returns a list of all the unique words in the document.
        """
        result = []
        for word in self._doc:
            if word not in result:
                result.append(word)
        return result

    def get_path(self):
        """
        Returns the path of the document.
        """
        return self._file_name
