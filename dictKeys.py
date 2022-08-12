#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: Alec Lowi
"""

#%% 1
# maybe write another function here...
def longest_path_length(d):
    length = 0
    for key in iter(d.keys()):
        keySet = []
        keylength = -1
        while key:
            if key in keySet:
                keylength += 1
                break
            keySet.append(key)
            key = d.get(key, False)
            keylength += 1
        if keylength > length:
            length = keylength
    return length

#%% 2
def large_value_keys(d, N):
    words = []
    for word,num in d.items():
        if N < num:
            words.append(word)
    words = words[::-1]
    return words

#%% 3
def count_words(filename):
    with open(filename, encoding='utf-8') as f:
        novel = f.read()
    novel = novel.lower()
    novel = novel.replace('-',' ')
    novel = novel.replace('——',' ')
    novel = novel.split()
    index = 0
    for word in novel:
        word.strip()
    for word in novel:
        if word.isnumeric():
            novel.pop(index)
   # print(novel)
    for word in novel:
        for c in word:
                if not c.isalpha():
                    x = word.replace(c, '')
                    novel[index] = x
                    if x is None or x == ' ':
                        novel.pop(index)
        index += 1
    word_dict = {}
    for word in novel:
        if not word in word_dict.keys():
            word_dict[word] = novel.count(word)
    return word_dict
