#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

re_header_line = re.compile(r'(\w+?): ?(.*)$')
re_entry = re.compile(r'^[^\t]')
re_entry_split = re.compile(r'^([^\t]*)\t([^\t]*)\t([^\t]*)\n')
re_meaning = re.compile(r'^\t[^\t]')
re_meaning_split = re.compile(r'^\t([^\t]*)\n')
re_ue = re.compile(r'^\t\t[^\t]')
re_ue_split = re.compile(r'^\t\t([^\t]*)\t([^\t]*)\n')

SENTENCE = 0
PHRASE = 1
CORPUS = 0
DICTIONARY = 1
FORMAT_TABS = 0

class DictionaryEntry(object):
    """docstring for DictionaryEntry"""
    def __init__(self, kana, kanji, entry_number):
        super(DictionaryEntry, self).__init__()
        self.kana = kana
        self.kanji = kanji # is a list
        self.entry_number = entry_number
        self.meanings = list()

    def add_meaning(self, meaning):
        """docstring for add_meaning"""
        self.meanings.append(meaning)

    def num_meanings(self):
        """docstring for num_meanings"""
        return len(self.meanings)

    def __str__(self):
        meaning_str_list = list()
        for m in self.meanings:
            meaning_str_list.extend(str(m).split('\n'))
        meaning_str = '\n'.join(["\t{}".format(m) 
                                 for m in meaning_str_list])
        kanji_str = u'・'.join(self.kanji)
        return ("{} {} [{}]\n{}".format(self.kana.encode('utf-8'), 
                                    self.entry_number, 
                                    kanji_str.encode('utf-8'),
                                    meaning_str)) 


class DictionaryMeaning(object):
    """docstring for DictionaryMeaning"""
    def __init__(self, meaning, meaning_number):
        super(DictionaryMeaning, self).__init__()
        self.meaning = meaning
        self.meaning_number = meaning_number
        self.usage_examples = list()

    def add_usage_example(self, ue):
        """docstring for add_ue"""
        self.usage_examples.append(ue)

    def __str__(self):
        ue_str_list = list()
        for ue in self.usage_examples:
            ue_str_list.extend(str(ue).split('\n'))
        ue_str = '\n'.join(["\t{}".format(ue) for ue in ue_str_list])
        return ("{}: {}\n{}".format(self.meaning_number, 
                                self.meaning.encode('utf-8'),
                                ue_str))


class UsageExample(object):
    """docstring for UsageExample"""
    def __init__(self, expression, meaning, type_=SENTENCE):
        super(UsageExample, self).__init__()
        self.expression = expression
        self.meaning = meaning
        self.type_ = type_

    def __str__(self):
        return ("{}\n{}".format(self.expression.encode('utf-8'),
                                self.meaning.encode('utf-8')))

class UELibraryImporter(object):
    """Imports usage example libraries"""
    def __init__(self, file_, encoding='utf-8'):
        super(UELibraryImporter, self).__init__()
        self.fh = codecs.open(file_, 'r', encoding=encoding)
        self.name = ''
        self.type_ = CORPUS
        self.format_type = FORMAT_TABS
        self.process_headers()
        self.prev_line = self.fh.readline()
        print self.name, self.type_, self.format_type

    def process_headers(self):
        """docstring for process_headers"""
        for line in self.fh:
            line = line.rstrip()
            if line == '':
                break
            m = re_header_line.match(line)
            if m:
                key = m.group(1)
                val = m.group(2)
                if key == 'NAME':
                    self.name = val
                elif key == 'TYPE':
                    if val.upper() == 'DICTIONARY':
                        self.type_ = DICTIONARY
                    else:
                        self.type_ == CORPUS
                elif key == 'FORMAT':
                    if val.upper() == 'TABS':
                        self.format_type = FORMAT_TABS

    def read_entry(self):
        """docstring for read_entry"""
        lines = list()
        for line in self.fh:
            #print self.prev_line,
            lines.append(self.prev_line)
            self.prev_line = line
            if re_entry.match(line):
                break
        return self.parse_entry_lines(lines)

    def parse_entry_lines(self, lines):
        """docstring for parse_entry_lines"""
        entry = None
        for line in lines:
            if re_entry.match(line):
                #print "entry", line,
                m = re_entry_split.match(line)
                entry = DictionaryEntry(m.group(1), m.group(2).split('|'), 
                                        m.group(3))
            elif re_meaning.match(line):
                #print "meaning", line,
                m = re_meaning_split.match(line)
                meaning_no = entry.num_meanings()+1
                meaning = DictionaryMeaning(m.group(1), meaning_no)
                entry.add_meaning(meaning)
                #print meaning
            elif re_ue.match(line):
                #print "ue", line,
                m = re_ue_split.match(line)
                ue = UsageExample(m.group(1), m.group(2))
                meaning.add_usage_example(ue)
                #print ue
        print entry
        return entry

def main():
    importer = UELibraryImporter('out2')
    lib_type = importer.type_
    entry = True
    while entry is not None:
        entry = importer.read_entry()
    #importer.read_entry()
    #importer.read_entry()
    #if lib_type == DICTIONARY:
        #while importer.not_end_of_file():
            #entry = importer.read_entry()
            #db_interface.import_entry(entry)

if __name__ == '__main__':
    main()
