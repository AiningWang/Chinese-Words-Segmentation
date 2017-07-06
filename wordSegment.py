# -*- coding: utf-8 -*-
import re
import sys

LENGTH      = 4
PMI_VALUE   = 24
INPUT_FILE  = "news_Feb.txt"


class Preprosess:
    def __init__(self):
        self.word_freq_dict = {}


    def wordFreq(self, text):
        """
            get all single word freq
        """
        text    = text.decode("utf8")
        # store chinese
        pattern = re.compile(u"([\u4e00-\u9fff]+)")
        chinese = pattern.findall(text)
        text    = ""
        for sentence in chinese:
            text += sentence
        # get word freq
        for i in range(len(text)):
            if text[i] not in self.word_freq_dict:
                self.word_freq_dict[text[i]] = 1
            else:
                self.word_freq_dict[text[i]] += 1


    def testWordFreq(self):
        """
            test func wordFreq
        """
        file1 = open("news_Feb.txt", "r")
        file2 = open("outcome.txt", "w")
        # get test text
        text = ""
        i = 0
        for line in file1:
            i += 1
            if i == 100:
                break
            text += line
        self.wordFreq(text)
        # output outcome
        for key in self.word_freq_dict:
            file2.write((key + " " + str(c.word_freq_dict[key]) + "\t").encode("utf8"))
        file2.close()






class WordInfo:
    def __init__(self, word):
        self.word   = word
        self.freq   = 0
        self.PMI    = 0
        self.left   = []
        self.right  = []
        self.left_entropy   = 0
        self.right_entropy  = 0


class WordSegment:
    def __init__(self):
        self.score = 0






# test
c = Preprosess()
c.wordFreq(text)







