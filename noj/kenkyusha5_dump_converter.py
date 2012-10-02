#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

re_entry = re.compile(ur'ﾛｰﾏ')
re_entry_split1 = re.compile(ur'^(.*?)([ 【].*$)')
re_entry_split2 = re.compile(ur'^(.*?)([１２３４５６７８９０]*)$')
re_entry_split3 = re.compile(ur'【(.*?)】')
re_entry_word_sep = re.compile(ur'・')
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

def split_entry(entry_line):
    m1 = re_entry_split1.match(entry_line)
    if m1:
        kana_and_number = m1.group(1)
        kanji_and_stuff = m1.group(2)
        m2 = re_entry_split2.match(kana_and_number)
        if m2:
            kana = m2.group(1)
            # number of word seps to skip for kanji
            num_sep = len(re_entry_word_sep.findall(kana))
            number = m2.group(2)
            if number == '':
                number = None
            else:
                number = int(number)
        else:
            raise Exception("didn't match split2")

        kanji = None
        m3 = re_entry_split3.search(kanji_and_stuff)
        if m3:
            kanji = list()
            kanji_unsplit = m3.group(1)
            kanji_over_split = re_entry_word_sep.split(kanji_unsplit)
            build_kanji = list()
            for k in kanji_over_split:
                build_kanji.append(k)
                if len(build_kanji) == num_sep+1:
                    kanji.append(u'・'.join(build_kanji))
                    build_kanji = list()
    else:
        raise Exception("didn't match split1")
    return {'kana':kana, 'number':number, 'kanji':kanji}

def match_sentence(line):
    if re_example_sentence.search(line):
        if (re_example_sentence_filter1.search(line) is None
            and
            re_example_sentence_filter2.match(line) is None):
            m = re_ue.match(line)
            return m
    return None

def entry_string(kana, number, kanji):
    """forming a string for an entry"""
    out = list()
    out.append(kana)
    if kanji is None:
        out.append('')
    else:
        out.append('|'.join(kanji))
    if number is None:
        out.append('')
    else:
        out.append(str(number))
    return '\t'.join(out)

#formation, phrase
f = codecs.open('wadai5.dump', 'r', encoding='utf-8')
print "NAME: Kenkyusha's New Japanese-English Dictionary 5th"
print "TYPE: DICTIONARY"
print "FORMAT: TABS"
print "KANJI-SEP: PIPE"
print
for line in f:
    #line = line.decode('utf-8')
    if line == '\n':
        continue
    if re_entry.search(line):
        in_entry = True
        in_meaning = False
        in_word_form = False
        has_multiple_meanings = True
        e = split_entry(line)
        print entry_string(kana=e['kana'], 
                number=e['number'], kanji=e['kanji']).encode('utf-8')
        #print "{}".format(line.encode('utf-8')),
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
                print "\t\t{}\t{}".format(
                        m.group(1).encode('utf-8'), 
                        m.group(2).encode('utf-8'))
            else:
                print "\t{}".format(line.encode('utf-8')),
        elif in_meaning == True:
            m = match_sentence(line)
            if m:
                print "\t\t{}\t{}".format(
                        m.group(1).encode('utf-8'), 
                        m.group(2).encode('utf-8'))
            #else:
                #print "\t\t<P>{}".format(line),

