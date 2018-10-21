import re
import unittest

def sumNums(fileName):
    inFile = open(fileName, 'r')
    lines = inFile.read()
    numbers = []
    find_num = re.findall('[0-9]+', lines)
    print(find_num)
    numbers = [int(nums) for nums in find_num]
    amount = sum(numbers)
    return amount



def countWord(fileName, word):
    inFile = open(fileName, 'r')
    read = inFile.read()
    find_word = []
    # count = 0
    file = read.strip()
    find_word = re.findall(word+('\\b'),file, re.IGNORECASE)
    print(find_word)
    total = len(find_word)
    return total

countWord("regex_sum_42.txt",'computer')

def listURLs(fileName):
    inFile = open(fileName, 'r')
    file = inFile.read()
    find_URL = re.findall('www.', file)
    return find_URL

listURLs("regex_sum_42.txt")



class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
