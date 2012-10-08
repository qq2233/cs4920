#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs
from japanese_parser import *
from data_structures import *
from db_interface import *
import sqlite3 as lite

re_header_line = re.compile(r'(\w+?): ?(.*)$')
re_entry = re.compile(r'^[^\t]')
re_entry_split = re.compile(r'^([^\t]*)\t([^\t]*)\t([^\t]*)\n')
re_meaning = re.compile(r'^\t[^\t]')
re_meaning_split = re.compile(r'^\t([^\t]*)\n')
re_ue = re.compile(r'^\t\t[^\t]')
re_ue_split = re.compile(r'^\t\t([^\t]*)\t([^\t]*)\n')


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
        return entry

    def entries(self):
        entry = self.read_entry()
        while entry is not None:
            yield entry
            entry = self.read_entry()

def import_library():
    """docstring for import_library"""
    importer = UELibraryImporter('out2')
    parser = JapaneseParser()
    lib_type = importer.type_
    con = lite.connect('sentence_library.db')
    cur = con.cursor() 
    try:
        cur.execute("INSERT INTO Libraries VALUES(null,?,?)",
                    ('Kenkyusha 5th', 1))
        lib_id = cur.lastrowid
        con.commit()
    except lite.IntegrityError as e:
        cur.execute("select id from Libraries as L where L.name = ?",
                ['Kenkyusha 5th'])    
        lib_id = cur.fetchone()[0]
    print lib_id
    i = 0
    for entry in importer.entries():
        print entry
        try:
            cur.execute("INSERT INTO Morphemes VALUES(null,?,?,?)",
                        (entry.kana, 15, None))
            kana_id = cur.lastrowid
        except lite.IntegrityError as e:
            cur.execute("select id from Morphemes as M where M.morpheme = ? and M.morphemeType = ?",
                    (entry.kana, 15))
            kana_id = cur.fetchone()[0]
        cur.execute("INSERT INTO Entries VALUES(null,?,?,?)",
                    (lib_id, entry.entry_number, kana_id))
        entry_id = cur.lastrowid
        #insert kanji
        for kanji in entry.kanji:
            if kanji == '':
                continue
            try:
                cur.execute("INSERT INTO Morphemes VALUES(null,?,?,?)",
                            (kanji, 14, None))
                kanji_id = cur.lastrowid
            except lite.IntegrityError as e:
                cur.execute("select id from Morphemes as M where M.morpheme = ? and M.morphemeType = ?",
                        (kanji, 14))
                kanji_id = cur.fetchone()[0]
            cur.execute("INSERT INTO EntryHasKanji VALUES(?,?)",
                        (entry_id, kanji_id))
        #insert meanings
        for meaning in entry.meanings:
            cur.execute("INSERT INTO Meanings VALUES(null,?,?)",
                        (meaning.meaning, entry_id))
            meaning_id = cur.lastrowid
            #insert UEs
            for ue in meaning.usage_examples:
                cur.execute("INSERT INTO UsageExamples VALUES(null,?,?,?,?)",
                            (ue.expression, ue.meaning, None, True))
                ue_id = cur.lastrowid
                cur.execute("INSERT INTO MeaningHasUEs VALUES(?,?)",
                            (ue_id, meaning_id))
                cur.execute("INSERT INTO UEPartOfLibrary VALUES(?,?)",
                            (ue_id, lib_id))
                components = ue.get_components(parser)

                #print listDictString(components)
                for component in components:
                    #print component['morpheme']
                    #print component
                    if component['base'] == '':
                        continue
                    try:
                        cur.execute("INSERT INTO Morphemes VALUES(null,?,?,?)",
                                    (component['base'], component['type'], None))
                        morph_id = cur.lastrowid
                    except lite.IntegrityError as e:
                        cur.execute("select id from Morphemes as M where M.morpheme = ? and M.morphemeType = ?",
                                (component['base'], component['type']))
                        morph_id = cur.fetchone()[0]
                    cur.execute("INSERT INTO UEConsistsOf VALUES(?,?,?,?)",
                                (ue_id, morph_id, component['length'], component['position']))

                    

        con.commit()
        #return
        #if i == 100:
            #return
        print i
        i += 1
    con.close()

def main():
    import_library()
    exit()
    importer = UELibraryImporter('out2')
    lib_type = importer.type_
    #entry = True
    #for entry in importer.entries():
        #print entry
    entry = importer.read_entry()
    print entry
    ue = entry.meanings[2].usage_examples[0]
    parser = JapaneseParser()
    print listDictString(ue.get_components(parser))
    #importer.read_entry()
    #if lib_type == DICTIONARY:
        #while importer.not_end_of_file():
            #entry = importer.read_entry()
            #db_interface.import_entry(entry)
    #db = DatabaseInterface()
    #db.new_library()
    #foreach entry in entries
        #insert into new library

    #kana_entry_type_id = get id for kana entry
    #kanji_entry_type_id = get id for kanji entry
    #lib_name = get name of library
    #lib_type = get id for dictionary type
    #lib_id = INSERT INTO Libraries VALUES (null, lib_name, lib_type)
    #foreach entry
        #if kana morph does not exist
            #kana_id = INSERT INTO Morphemes VALUES (null, entry.kana, 
                    #kana_entry_id, null)
        #entry_id = INSERT INTO Entries VALUES (null, lib_id, entry.number, kana_id)
        #kanji_id_list = get the kanjis id (lazy)
        #for each kanji_id in kanji_id_list
            #INSERT INTO EntryHasKanji VALUES (entry_id, kanji_id)
        #insert the meanings
        

        


if __name__ == '__main__':
    main()
