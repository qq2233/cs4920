#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

re_entry = re.compile(ur'ﾛｰﾏ')
re_ue = re.compile(ur'^[▲・◧◨]?(.*)　(.*)$')
re_numbered_meaning = re.compile(ur'^[0-9]+ ')
re_example_sentence = re.compile(ur'[.」!?]　')
re_example_sentence_filter1 = re.compile(ur'<LINK>')
re_example_sentence_filter2 = re.compile(ur'^…')
#re_word_form = re.compile(r'^[^　]*$')

has_multiple_meanings = False
entry_number = 0
in_entry = False
in_meaning = False
#in_word_form = False

def match_sentence(line):
    if re_example_sentence.search(line):
        if (re_example_sentence_filter1.search(line) is None
            and
            re_example_sentence_filter2.match(line) is None):
            m = re_ue.match(line)
            return m
    return None

#formation, phrase
f = codecs.open('wadai5.dump', 'r', encoding='utf-8')
for line in f:
    #line = line.decode('utf-8')
    if line == '\n':
        continue
    if re_entry.search(line):
        in_entry = True
        in_meaning = False
        in_word_form = False
        has_multiple_meanings = True
        print "{}".format(line.encode('utf-8')),
    elif in_entry == True:
        if (re_numbered_meaning.match(line) and 
                has_multiple_meanings == True):
            in_meaning = True
            in_word_form = False
            print "\t{}".format(line.encode('utf-8')),
        elif in_meaning == False:
            has_multiple_meanings = False
            in_meaning = True
            in_word_form = False
            m = match_sentence(line)
            if m:
                print "\t"
                print "\t\t<E>{}<M>{}".format(
                        m.group(1).encode('utf-8'), 
                        m.group(2).encode('utf-8'))
            else:
                print "\t{}".format(line.encode('utf-8')),
        elif in_meaning == True:
            m = match_sentence(line)
            if m:
                print "\t\t<E>{}<M>{}".format(
                        m.group(1).encode('utf-8'), 
                        m.group(2).encode('utf-8'))
            #else:
                #print "\t\t<P>{}".format(line),

