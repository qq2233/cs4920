#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import re
import codecs
from japanese_parser import *
from data_structures import *
from db_interface import *
from kenkyusha5_dumper import *
from kenkyusha5_dump_converter import *
import sqlite3 as lite

re_header_line = re.compile(r'(\w+?): ?(.*)$')
re_entry = re.compile(r'^[^\t]')
re_entry_split = re.compile(r'^([^\t]*)\t([^\t]*)\t([^\t]*)\n')
re_meaning = re.compile(r'^\t[^\t]')
re_meaning_split = re.compile(r'^\t([^\t]*)\n')
re_ue = re.compile(r'^\t\t[^\t]')
re_ue_split = re.compile(r'^\t\t([^\t]*)\t([^\t]*)\n')

class LibraryImporter(object):
    """docstring for LibraryImporter"""
    def __init__(self):
        super(LibraryImporter, self).__init__()

    def set_library(self, library_code):
        """docstring for set_library"""
        self.library_code = library_code
        
    def prepare_library(self):
        """docstring for prepare"""
        if self.library_code == 'WADAI5':
            dumper = Kenkyusha5Dumper('kenkyusha')
            dumper.dump('kenkyusha_dump')
            dump_converter = Kenkyusha5DumpConverter('kenkyusha_dump')
            dump_converter.convert('kenkyusha_converted')
    
    def import_progress(self):
        """docstring for import_progress"""
        progress = ProgressPoint(1, 2, 0, 1)
        yield progress
        self.prepare_library()
        dbi = DatabaseInterface('sentence_library2.db')
        dbi.reset_database()
        importer = UELibraryImporter('out2')
        parser = JapaneseParser()
        lib_type = importer.type_
        lib_id = dbi.get_or_create_library_id('Kenkyusha 5th', 1)
        print lib_id
        total_num_entries = num_entries('out2')
        progress = ProgressPoint(2, 2, 0, total_num_entries)
        for idx, entry in enumerate(importer.entries()):
            #print entry
            progress.point = idx
            dbi.import_entry_recursive(entry, lib_id, parser)
            #yield idx
            yield progress
        dbi.commit()

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
        self.library_code = None
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
    dbi = DatabaseInterface('sentence_library2.db')
    dbi.reset_database()
    importer = UELibraryImporter('out2')
    parser = JapaneseParser()
    lib_type = importer.type_
    lib_id = dbi.get_or_create_library_id('Kenkyusha 5th', 1)
    print lib_id
    for idx, entry in enumerate(importer.entries()):
        print entry
        dbi.import_entry_recursive(entry, lib_id, parser)
        print idx
    dbi.commit()

def num_entries(fname):
    num_entries = 0
    with open(fname) as fh:
        for line in fh:
            if re_entry.match(line):
                num_entries += 1
    return num_entries


#def import_progress():
    #"""docstring for import_progress"""
    #dbi = DatabaseInterface('sentence_library2.db')
    #dbi.reset_database()
    #importer = UELibraryImporter('out2')
    #parser = JapaneseParser()
    #lib_type = importer.type_
    #lib_id = dbi.get_or_create_library_id('Kenkyusha 5th', 1)
    #print lib_id
    #total_num_entries = num_entries('out2')
    #progress = ProgressPoint(1, 2, 0, total_num_entries)
    #for idx, entry in enumerate(importer.entries()):
        ##print entry
        #progress.point = idx
        #dbi.import_entry_recursive(entry, lib_id, parser)
        ##yield idx
        #yield progress
    #dbi.commit()

class ProgressPoint(object):
    """docstring for ProgressPoint"""
    def __init__(self, phase, total_phases, point, total_points):
        super(ProgressPoint, self).__init__()
        self.total_phases = total_phases
        self.phase = phase
        self.point = point
        self.total_points = total_points

    def percent(self):
        return (self.point / self.total_points) * 100

    def __str__(self):
        """docstring for __str__"""
        return "Phase {}/{}  {:3.2f}% {}".format(self.phase, 
                                         self.total_phases, 
                                         self.percent(),
                                         self.point)

def main():
    #import_library()
    #for progress in import_progress():
        #print progress
    importer = LibraryImporter()
    importer.set_library('WADAI5')
    #importer.prepare_library()
    for progress in importer.import_progress():
        print progress

if __name__ == '__main__':
    main()
