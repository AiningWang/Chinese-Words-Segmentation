# -*- coding: utf-8 -*-

"""
    Chinese word segmentation
    Author: Aining Wang
    Date:   07/2017
"""

import re
import sys
from MathTool import entropy, Counter


WORD_LEN    = [1,2,3,4,5,6]
ENT_VALUE   = 1000
AGG_VALUE   = 1000
FREQ        = 5
INPUT_FILE  = "AI_news.txt"


class WordInfo:
    
    def __init__(self, word, freq):
        self.word           = word
        self.length         = len(word)
        self.freq           = freq
        self.aggregation    = 0    # Internal aggregation degree
        self.left_dict      = {}   # {left word: freq}
        self.right_dict     = {}   # {right word: freq}
        self.entropy        = 0    # External using freedom
        self.score          = 0
    

    def turnDictToLict(self):
        for word in self.left_dict:
            self.left_prob_list.append(self.left_dict[word])
        for word in self.right_dict:
            self.right_prob_list.append(self.right_dict[word])


    def calculateEntropy(self):
        # turn dict to list
        left_prob_list = []
        right_prob_list = []
        for word in self.left_dict:
            left_prob_list.append(self.left_dict[word])
        for word in self.right_dict:
            right_prob_list.append(self.right_dict[word])
        # calculate entropy
        self.entropy = min(entropy(left_prob_list), entropy(right_prob_list))


    def calculateAggregation(self, word_freq_dict):
        ent_record = []
        for i in range(self.length - 1):
            word1 = self.word[i + 1 :]
            word2 = self.word[: i + 1]
            ent = entropy([word_freq_dict[self.word], word_freq_dict[word1] * word_freq_dict[word2]])
            ent_record.append(ent)
        self.aggregation = min(ent_record)



class WordSegment:
    
    def __init__(self):
        self.candidate_dict = {}  # length 2-5
        self.text           = ""
        self.word_freq      = {}  # count word freq (length between 1-6)
        self.new_word_list  = []


    def getInputText(self):
        file        = open(INPUT_FILE, "r")
        pattern     = re.compile(u"([\u4e00-\u9fff]+)")
        origin_text = ""
        for line in file:
            origin_text += line
        # get chinese words
        origin_text = origin_text.decode("utf8")
        chinese     = pattern.findall(origin_text)
        for sentence in chinese:
            self.text += sentence


    def countWordFreq(self):
        self.getInputText()
        # count word freq
        for word_length in WORD_LEN:
            print word_length
            for i in range(len(self.text) - word_length):
                Counter(self.text[i : i+word_length], self.word_freq)
        # output outcome
        file2 = open("word_freq.txt", "w")
        for key in self.word_freq:
            file2.write((key + " " + str(self.word_freq[key]) + "\t").encode("utf8"))
        file2.close()


    def setCandidateWord(self):
        # set words as candidates (freq > 1, 1 < len < 6):
        for word in self.word_freq:
            if len(word) > 1 and len(word) < 6 and self.word_freq[word] > 1:
                self.candidate_dict[word] = WordInfo(word, self.word_freq[word])
        # output outcome
        file = open("candidate.txt", "w")
        for key in self.candidate_dict:
            file.write((key + " " + str(self.candidate_dict[key].freq) + "\t").encode("utf8"))
        file.close()


    def collectLeftRightDict(self):
        for word in self.word_freq:
            if len(word) > 2:
                # find right words
                if word[: -1] in self.candidate_dict:
                    self.candidate_dict[word[: -1]].right_dict[word[-1]] = self.word_freq[word[-1]]
                # find left words
                elif word[1 :] in self.candidate_dict:
                    self.candidate_dict[word[1 :]].left_dict[word[0]] = self.word_freq[word[0]]


    def calculateCandidateScore(self):
        # calculate entropy and aggregation
        for word in self.candidate_dict:
            self.candidate_dict[word].calculateEntropy()
            self.candidate_dict[word].calculateAggregation(self.word_freq)
        # filter candidate
        self.new_word_list = []
        for word in self.candidate_dict:
            info = self.candidate_dict[word]
            if info.freq >= FREQ and info.aggregation >= AGG_VALUE and info.entropy >= ENT_VALUE:
                self.new_word_list.append(word)


    def execute(self):
        self.countWordFreq()
        self.setCandidateWord()
        self.collectLeftRightDict()
        self.calculateCandidateScore()
        # output outcome
        file = open("AI_new_word.txt", "w")
        for word in self.new_word_list:
            info = self.candidate_dict[word]
            file.write(word.encode("utf8") + "\n")
            print  str(info.freq) + "\t" + str(info.aggregation)  + "\t" + str(info.entropy)
        file.close()


# test
c = WordSegment()
c.execute()




