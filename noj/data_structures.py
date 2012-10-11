#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db_interface import *

SENTENCE = 0
PHRASE = 1
CORPUS = 0
DICTIONARY = 1
FORMAT_TABS = 0

class Dictionary(object):
    """docstring for Dictionary
A Dictionary contains a 'name' for the dictionary and a subsequent list of 'entries'.
"""
    def __init__(self, name):
        super(Dictionary, self).__init__()
        self.name = name
        self.entries = list()

#    def import_non_recursive(self, db_interface):
#        """docstring for import"""
#        db_interface.create_dictionary(self)
#        pass

#    def get_id(self, db_interface):
#        """docstring for import"""
#        pass
        

class DictionaryEntry(object):
    """docstring for DictionaryEntry

Creates Dictionary Entry structure which consists of 5 elements:

kana = How the Japanese word is pronounced (stored as string)
kanji = The entry in proper Japanese form (sotred as list)
entry_number = ID number given to entry (stored as integer)
meanings = A list of meanings for the associated entry

"""
    def __init__(self, kana, kanji, entry_number):
        super(DictionaryEntry, self).__init__()
        self.kana = kana
        self.kanji = kanji # is a list
        self.entry_number = entry_number
        self.meanings = list()

    def add_meaning(self, meaning):
        """docstring for add_meaning
Add meaning to Dictionary Entry
NOTE: An entry can have multiple meanings
"""
        self.meanings.append(meaning)

    def num_meanings(self):
        """docstring for num_meanings
Returns the number of meanings for a Dictionary Entry as entries may have multiple meanings
"""
        return len(self.meanings)
    
    def __str__(self):

        meaning_str_list = list()
        for m in self.meanings:
            meaning_str_list.extend(str(m).split('\n'))
        meaning_str = '\n'.join(["\t{}".format(m) 
                                 for m in meaning_str_list])
        kanji_str = u'·'.join(self.kanji)
        return ("{} {} [{}]\n{}".format(self.kana.encode('utf-8'), 
                                    self.entry_number, 
                                    kanji_str.encode('utf-8'),
                                    meaning_str)) 

    def __repr__(self):

        lines = list()
        lines.append("e = DictionaryEntry({}, {}, {})".format(
                     repr(self.kana), repr(self.kanji), 
                     repr(self.entry_number)))
        for meaning in self.meanings:
            lines.append(repr(meaning))
            lines.append("e.add_meaning(m)")
        return '\n'.join(lines)


class DictionaryMeaning(object):
    """docstring for DictionaryMeaning
    
A Dictionary Entry may have a Dictionary Meaning

A Dictionary Meaning has 3 elements:

meaning = the definition
meaning_number = as there might be multiple meanings, this will keep track
usage_examples = a list of usage examples that use this dictionary meaning(optional)
"""
    def __init__(self, meaning, meaning_number):
        super(DictionaryMeaning, self).__init__()
        self.meaning = meaning
        self.meaning_number = meaning_number
        self.usage_examples = list()

    def add_usage_example(self, ue):
        """docstring for add_ue

Helper function that appends usage examples to Dictionary Meaning"""
        self.usage_examples.append(ue)

    def __str__(self):
        ue_str_list = list()
        for ue in self.usage_examples:
            ue_str_list.extend(str(ue).split('\n'))
        ue_str = '\n'.join(["\t{}".format(ue) for ue in ue_str_list])
        return ("{}: {}\n{}".format(self.meaning_number, 
                                self.meaning.encode('utf-8'),
                                ue_str))

    def __repr__(self):
        lines = list()
        lines.append("m = DictionaryMeaning({}, {})".format(
                     repr(self.meaning), repr(self.meaning_number)))
        for ue in self.usage_examples:
            lines.append(repr(ue))
            lines.append('m.add_usage_example(ue)')
        return '\n'.join(lines)


class UsageExample(object):
    """docstring for UsageExample
	
An usage example is a sentence that is associated with a particular word

This class has 4 elements:

expression =  the sentence itself
meaning = the meaning of the word assocaited witht he usage example
type = is this a sentence or phase -> default is sentence
components = what are the break up of words in the sentence
"""
    def __init__(self, expression, meaning, type_=SENTENCE):
        super(UsageExample, self).__init__()
        self.expression = expression
        self.meaning = meaning
        self.type_ = type_ --> sentence or phrase --> defaults to sentence
        self.components = None

    def get_components(self, parser):
        """docstring for get_components

Places words that belong to the usage example as a list
"""
        if self.components is None:
            self.components = parser.parse(self.expression).components 
        return self.components

    def __str__(self):
        return ("{}\n{}".format(self.expression.encode('utf-8'),
                                self.meaning.encode('utf-8')))

    def __repr__(self):
        lines = list()
        lines.append("ue = UsageExample({}, {}, {})".format(
                     repr(self.expression), repr(self.meaning), 
                     repr(self.type_)))
        return '\n'.join(lines)

if __name__ == '__main__':
    db_interface = DatabaseInterface('sentence_library.db')
    dictionary = Dictionary('Test Dict')
    dictionary.import_non_recursive(db_interface)
