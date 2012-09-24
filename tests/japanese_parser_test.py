# -*- coding: utf-8 -*-
import unittest
from noj import japanese_parser

expression1='今日もしないとね。'
expectedAnkiReading1='今日[きょう]もしないとね。'
expectedComponents1 = [
    {'morpheme':'今日', 'base':'今日', 'reading': 
        'きょう', 'position': 0, 'length': 6, 
        'type':japanese_parser.NOUN}, 
    {'morpheme':'も', 'base':'も', 'reading': 
        'も', 'position': 6, 'length': 3, 
        'type':japanese_parser.PARTICLE}, 
    {'morpheme':'し', 'base':'する', 'reading': 
        'し', 'position': 9, 'length': 3, 
        'type':japanese_parser.VERB}, 
    {'morpheme':'ない', 'base':'ない', 'reading': 
        'ない', 'position': 12, 'length': 6, 
        'type':japanese_parser.AUXILIARY_VERB}, 
    {'morpheme':'と', 'base':'と', 'reading': 
        'と', 'position': 18, 'length': 3, 
        'type':japanese_parser.PARTICLE}, 
    {'morpheme':'ね', 'base':'ね', 'reading': 
        'ね', 'position': 21, 'length': 3, 
        'type':japanese_parser.PARTICLE}
]
expression2='明日は今日よりやや暖かいでしょう.'
expectedAnkiReading2='明日[あした]は 今日[きょう]よりやや 暖[あたた]かいでしょう.'

class MyTest(unittest.TestCase):

    #def testMethod(self):
        #self.assertEqual(1 + 2, 3, "1 + 2 not equal to 3")

    def testParse1(self):
        parser = japanese_parser.JapaneseParser()
        results = parser.parse(expression1)
        self.assertEqual(results.components(), expectedComponents1, 
                "parse components mismatch")
        self.assertEqual(results.ankiReading(), expectedAnkiReading1, "parse anki readings mismatch")

    def testParse2(self):
        parser = japanese_parser.JapaneseParser()
        results = parser.parse(expression2)
        self.assertEqual(results.ankiReading(), expectedAnkiReading2, 
                "parse anki readings mismatch")

    #texts = "自動 生成されています."

if __name__ == '__main__':
    unittest.main()
