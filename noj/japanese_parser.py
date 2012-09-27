# -*- coding: utf-8 -*-
# code adapted from:
# http://mecab.googlecode.com/svn/trunk/mecab/doc/bindings.html
# https://github.com/dae/ankiplugins/blob/master/japanese/reading.py

from __future__ import print_function
import MeCab
import re
from jcconv import *

BOS_EOS = 0
INTERJECTION = 1
ADVERB = 2
PRE_NOUN_ADJECTIVAL = 3
NOUN = 4
AUXILIARY_VERB = 5
VERB = 6
PARTICLE = 7
PREFIX = 8
ADJECTIVE = 9
CONJUNCTION = 10
FILLER = 11
SYMBOL = 12
OTHER = 13

morphemeTypes = {
    'BOS/EOS':BOS_EOS,
    '感動詞':INTERJECTION,
    '副詞':ADVERB,
    '連体詞':PRE_NOUN_ADJECTIVAL,
    '名詞':NOUN,
    '助動詞':AUXILIARY_VERB,
    '動詞':VERB,
    '助詞':PARTICLE,
    '接頭詞':PREFIX,
    '形容詞':ADJECTIVE,
    '接続詞':CONJUNCTION,
    'フィラー':FILLER,
    '記号':SYMBOL,
    'その他':OTHER,
}

class JapaneseParser(object):
    """A MeCab parser to parse japanese sentences into morphemes"""
    def __init__(self):
        super(JapaneseParser, self).__init__()
        self._parser = None
        self.skipTypes = frozenset([BOS_EOS])

    def parse(self, expression):
        """Parse a japanese expression into morphemes, returns 
        parse results"""
        node = self.parser.parseToNode(expression)
        results = JapaneseParseResults()
        position = 0
        while node:
            details = re.split(',', node.feature)
            for d in range(0,len(details)):
                if details[d] == '*':
                    details[d] = ''
            type = morphemeTypes[details[0]]
            if type not in self.skipTypes:
                results.addMorpheme (
                    morpheme=node.surface,
                    base=details[-3],
                    reading=kata2hira(details[-2]),
                    length=node.length,
                    position=(node.rlength-node.length)+position,
                    type=type
                )
            position = position + node.rlength
            node = node.next
        return results

    @property
    def parser(self):
        """Get the parser lazily"""
        if not self._parser:
            self._parser = MeCab.Tagger('mecabrc')
        return self._parser

class JapaneseParseResults(object):
    """Results from parsing using Japanese Parser"""
    def __init__(self):
        super(JapaneseParseResults, self).__init__()
        self.morphemes = list()
        self.skipTypesComponents = frozenset([BOS_EOS, SYMBOL])
        self._components = None

    def addMorpheme(self, morpheme, base=None, reading=None, 
            length=None, position=None, type=None):
        """add a morpheme to the parse results"""
        m = {
            'morpheme':morpheme,
            'base':base,
            'reading':reading,
            'length':length,
            'position':position,
            'type':type,
        }
        self.morphemes.append(m)

    # Don't use this function yet, will modify when we get to using it
    def ankiReading(self):
        """return string compatible with anki for furigana reading
        See: https://github.com/dae/ankiplugins
                /blob/master/japanese/reading.py"""
        out = []
        for idx, m in enumerate(self.morphemes):
            # hiragana, punctuation, not japanese, or lacking a reading
            morpheme = m['morpheme']
            reading = m['reading']
            if morpheme == reading or not reading or reading == '':
                out.append(morpheme)
                continue
            # katakana
            # TODO:
            # don't add readings of numbers
            #if morpheme in u"一二三四五六七八九十０１２３４５６７８９":
                #out.append(morpheme)
                #continue

            # strip matching hiragana characters at beginning and 
            # end of morpheme. This code was adapted from the Anki
            # Japanese support library
            placeL = 0
            placeR = 0
            md = morpheme.decode('utf-8')
            rd = reading.decode('utf-8')
            for i in range(1,len(md)):
                if md[-i] != rd[-i]:
                    break
                placeR = i
            for i in range(0,len(md)-1):
                if md[i] != rd[i]:
                    break
                placeL = i+1
            if placeL == 0:
                if placeR == 0:
                    out.append((" %s[%s]" % (
                        md, rd)).encode('utf-8'))
                else:
                    out.append((" %s[%s]%s" % (
                        md[:-placeR], rd[:-placeR], 
                        rd[-placeR:])).encode('utf-8'))
            else:
                if placeR == 0:
                    out.append(("%s %s[%s]" % (
                        rd[:placeL], md[placeL:], 
                        rd[placeL:])).encode('utf-8'))
                else:
                    out.append(("%s %s[%s]%s" % (
                        rd[:placeL], md[placeL:-placeR],
                        rd[placeL:-placeR], 
                        rd[-placeR:])).encode('utf-8'))
        return ''.join(out).strip()

    @property
    def components(self):
        """return dict of morphemes which were part of the 
        original expression. Used for populating the database.
        Ignores characters which are too common and punctuation
        Uses lazy instantiation"""
        if self._components == None:
            self._components = list()
            for m in self.morphemes:
                if m['type'] not in self.skipTypesComponents:
                    self._components.append(m)
        return self._components

def listDictString(l):
    """Used for pretty printing japanese parse result components
    as directly printing out the data structure will not display
    utf-8 correctly"""
    out = list()
    for item in l:
        group = ['{']
        for key, value in item.items():
            valuePrint = value
            if not isinstance(value, int):
                valuePrint = "'{}'".format(value)
            group.append("'{}':{}, ".format(key, valuePrint))
        group.append('},')
        out.append(''.join(group))
    return '\n'.join(out)

        
if __name__ == "__main__":
    parser = JapaneseParser()
    results = parser.parse("明日は晴れるかな")
    #results = parser.parse("自動 生成されています.")
    #results = parser.parse("自動 生成されています.")
    #results = parser.parse("今日もしないとね。")
    #results = parser.parse('明日は今日よりやや暖かいでしょう.')
    #results = parser.parse('プログラムは一部2,000 円だ.')
    #results = parser.parse('データは以下のとおりです。')
    #results = parser.parse('This is english')
    print(listDictString(results.components))
    print("reading:{}".format(results.ankiReading()))
