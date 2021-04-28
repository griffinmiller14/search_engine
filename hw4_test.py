"""
Griffin Miller
CSE 163 AI
This program implements the test functions for
homework 4.
"""
from cse163_utils import assert_equals
import math
from document import Document
from search_engine import SearchEngine


def test_document(doc1, doc2, doc3, doc4):
    """
    Tests aspects of the Document class.
    """
    # test get words
    assert_equals({'griffin', 'miller'}, doc1.get_words())
    # test term frequency
    assert_equals(1/3, doc4.term_frequency('LiVeRpool'))
    # test get path
    assert_equals('test_docs/test4.txt', doc4.get_path())


def test_single(test1):
    """
    Test the implementation of single word queries for the search
    method and calculate idf method in the SearchEngine class.
    """
    # Test simple case
    assert_equals(['test_docs/test1.txt', 'test_docs/test2.txt'],
                  test1.search('griffin'))
    # Test with upper case and symbol search
    assert_equals(['test_docs/test1.txt', 'test_docs/test2.txt'],
                  test1.search('Grif!!fin'))
    # Test for a word that doesnt appear in any docs
    assert_equals(None, test1.search('Seattle'))
    # Test for idf (must be lowercase for testing)
    assert_equals(math.log(4/2), test1._calculate_idf('griffin'))
    # Test idf for a word that doesnt appear in any docs
    assert_equals(0, test1._calculate_idf('Seattle'))


def test_mulit(test1):
    """
    Test the implementation of multi word queires for the search
    method in the SearchEngine class.
    """
    # Test simple case
    assert_equals(['test_docs/test4.txt'], test1.search('football club'))
    # Test with upper case and symbols
    assert_equals(['test_docs/test1.txt', 'test_docs/test2.txt'],
                  test1.search('Grif!!fin mILL#####Er'))
    # Test for a word that doesnt appear in any docs
    assert_equals(None, test1.search('Seattle Mariners'))


def main():
    test1 = Document('test_docs/test1.txt')
    test2 = Document('test_docs/test2.txt')
    test3 = Document('test_docs/test3.txt')
    test4 = Document('test_docs/test4.txt')
    test_search1 = SearchEngine('test_docs')

    test_document(test1, test2, test3, test4)
    test_single(test_search1)
    test_mulit(test_search1)


if __name__ == '__main__':
    main()
