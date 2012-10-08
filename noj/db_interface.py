#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

class DatabaseInterface(object):
    def __init__(self, db_path):
        self.db_path = db_path
        self.con = lite.connect(self.db_path)
        self.lib_type_ids = dict()
        print("Connection Established")    
      
    def get_lib_type_id(self, type_name):
        """docstring for get_lib_type_id"""
        if type_name not in self.lib_type_ids:
            try:
                con = lite.connect(self.db_path)
                with con:
                    cur = con.cursor() 
                    cur.execute("select id from LibraryTypes as L where L.type = ?",[type_name])    
                    self.lib_type_ids[type_name] = cur.fetchone()[0]
            except lite.Error as e:
                if con:
                    con.rollback()
                print "Error %s:" % e.args[0]
                sys.exit(1)
            except TypeError as e:
                raise KeyError("No tuple for '{}' in LibraryTypes".format(type_name))
        return self.lib_type_ids[type_name]

    def create_dictionary(self,dictionary):
        try:
            con = lite.connect(self.db_path)
            with con:
                cur = con.cursor()    
                lib_type_id = self.get_lib_type_id('DICTIONARY')
                cur.execute("INSERT INTO Libraries VALUES(null,?,?)",
                            (dictionary.name, lib_type_id))
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)

    def import_UE(self,UsageExample,Meaning):
        try:
            con = lite.connect(self.db_path)
            with con:
                cur = con.cursor()    
                cur.execute("INSERT INTO UsageExamples VALUES(null,?,?,?,?)",(UsageExample.meaning,UsageExample.expression,UsageExample.reading,UsageExample.sentence))
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
 
    def searchUE_Dictionary(self,entry):
        try:
            con = lite.connect(self.db_path)
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select meaning from Meanings as M, EntryHasMeanings as EM, Entries as E where E.id = EM.entry and M.id = EM.meaning and EM.entry =?",(entry.id))    
                rows = cur.fetchall()
                for row in rows:
                    print "%s" % (row["meaning"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
 
                
    def searchUE_lookup(self,morpheme):
        try:
            con = lite.connect(self.db_path)
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select UE.id as id, UE.expression as expression, UE.meaning as meaning from UsageExamples as UE, UEConsistsOf as UEC, Morphemes as M where UE.id = UEC.usageExample and UEC.morpheme = M.id and M.morpheme = ?",(morpheme))
                rows = cur.fetchall()
                for row in rows:
                    print "%s %s %s" % (row["id"], row["expression"], row["meaning"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)       
    
    def storeUE_list(self,user_list):
        """Create an UE or Word List assumes and object of type user_list is passed as argument"""
        try:
            con = lite.connect(self.db_path)
            with con:
                cur = con.cursor()    
                nameOfList = user_list.name 
                typeOfList = user_list.type
                cur.execute("INSERT INTO Lists VALUES(null,?,?)",(nameOfList,typeOfList))
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
    
    def insert_elements(self,user_list,UsageExample):
        """Inserts Elements into the UE or Word List assumes an input arg of UsageExample & user_list Object"""
        try:
            con = lite.connect(self.db_path)
            with con:
                cur = con.cursor()    
                list_id = user_list.id
                UE_id = UsageExample.id        
                cur.execute("INSERT INTO UEPartOfList VALUES(?,?,'toLearn')",(list_id,UE_id))
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
    
    def retrieveUE_list(self,nameOfList):
        "Retreives an UE List, args expected name of List"
        try:
            con = lite.connect(self.db_path)
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select UE.id as id, UE.expression as expression, UE.meaning as meaning from UsageExamples as UE, UEPartOfList as UEL, List as L where UE.usageExample = UE.id and UEL.list = L.id and L.name = ?",(nameOfList))
                rows = cur.fetchall()
                for row in rows:
                    print "%s %s %s" % (row["id"], row["expression"], row["meaning"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
  
    def get_infoUE(self,UsageExample):
        """Input arg is an UE Object"""
        try:
            con = lite.connect("sentence_library.db")
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select * from UsageExamples as UE where UE.expression = ?",(UsageExample.expression))
                rows = cur.fetchall()
                for row in rows:
                    print "%s %s %s" % (row["id"], row["expression"], row["meaning"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
    
    def get_UESource(self,UsageExample):
        try:
            con = lite.connect("sentence_library.db")
            with con:
                con.row_factory = lite.Row
                cur = con.cursor() 
                cur.execute("select L.name as source from Library as L, Entries as E, EntryHasMeanings as EM, MeaningHasUEs as MUE, UsageExamples as UE, Meanings as M where L.id = E.library and EM.entry = E.id and EM.meaning = M.id and M.id = MUE.meaning and MUE.usageExample = UE.id and UE.expression = ?",(UsageExample.expression))
                rows = cur.fetchall()
                for row in rows:
                    print "%s " % (row["source"])
        except lite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
            
    
