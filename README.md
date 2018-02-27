# Chinese Words Segmentation 
## Dataset
* total 36497 chinese news, which is collected from the Internet
## Purpose
Different from English, there are no space between Chinese words. This project aims to implement Chinese word segmentation without dictionary.
* develop Chinese word segmentation algorithm based on entropy
* find new Chinese words (which is not in corpus)
## Method
### Chinese Words Segmentation
#### Internal Aggregation
* see WordInfo.calculateAggregation()
#### External Collocation Richness
* see WordInfo.calculateEntropy()
#### Word Frequency
##### If the word frequency is too high, it might be stop words.
##### If the word frequency is too low, it may not be as word. 
* In this project, I set FREQ_MIN = 5, FREQ_MAX = 10. The word between FREQ_MIN and FREQ_MAX can be new words candidates
## Usage
* Change INPUT_FILE in wordSegment.py
* python 2
