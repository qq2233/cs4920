#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

re_header_line = re.compile(r'(\w+?): ?(.*)$')
re_entry = re.compile(r'^[^\t]')

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

    def __str__(self):
        return ("{} {} [{}]".format(
            self.kana, self.entry_number, self.kanji))  


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

class UsageExample(object):
    """docstring for UsageExample"""
    def __init__(self, expression, meaning, type_=SENTENCE):
        super(UsageExample, self).__init__()
        self.expression = expression
        self.meaning = meaning
        self.type_ = type_

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
        in_entry = False
        for line in self.fh:
            print self.prev_line,
            if re_entry.match(self.prev_line):
                in_entry == True
            self.prev_line = line
            if re_entry.match(line):
                break

def main():
    importer = UELibraryImporter('out2')
    lib_type = importer.type_
    importer.read_entry()
    importer.read_entry()
    importer.read_entry()
    #if lib_type == DICTIONARY:
        #while importer.not_end_of_file():
            #entry = importer.read_entry()
            #db_interface.import_entry(entry)

if __name__ == '__main__':
    main()
