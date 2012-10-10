'''
Created on 08/10/2012

@author: sebastien
'''
import bassic


class control(object):
    '''
    classdocs
    '''


    def __init__(self, gui):
        '''
        Constructor
        '''
        self.mode = ""
        self.gui = gui
        
    def test(self, str):
        
        print str
        
    def search(self, str):
        print "a search for \"" + str + "\" was conducted"
        
        if (self.mode == "dictionary"):
            if (str):
                self.gui.dictionary_2.show()
                self.gui.DictionaryWordsScrollArea.hide()
            else:
                self.gui.dictionary_2.hide()
        else:    
            pass
        
            
    def lookUpMode(self, str):
        self.mode = "lookUp"
        self.gui.UEarea.show()
        self.gui.dictionary_2.hide()
        self.search(str)
        
    def dictionaryMode(self, str):
        self.mode = "dictionary"
        self.gui.dictionary_2.show()
        self.gui.UEarea.hide()
        self.search(str)
            
    def wordMeanings(self, str):
        print "button has been clicked linked to \"" +str+ "\" meaning"
        
        self.gui.DictionaryWordsScrollArea.show()
    