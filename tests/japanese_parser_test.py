# -*- coding: utf-8 -*-
import unittest
from noj import japanese_parser

expected = [
    {
        'expression':u'今日もしないとね。',
        'reading':u'今日[きょう]もしないとね。',
        'components':[
            {'morpheme':u'今日', 'base':u'今日', 'reading': 
                u'きょう', 'position': 0, 'length': 6, 
                'type':japanese_parser.NOUN}, 
            {'morpheme':u'も', 'base':u'も', 'reading': 
                u'も', 'position': 6, 'length': 3, 
                'type':japanese_parser.PARTICLE}, 
            {'morpheme':u'し', 'base':u'する', 'reading': 
                u'し', 'position': 9, 'length': 3, 
                'type':japanese_parser.VERB}, 
            {'morpheme':u'ない', 'base':u'ない', 'reading': 
                u'ない', 'position': 12, 'length': 6, 
                'type':japanese_parser.AUXILIARY_VERB}, 
            {'morpheme':u'と', 'base':u'と', 'reading': 
                u'と', 'position': 18, 'length': 3, 
                'type':japanese_parser.PARTICLE}, 
            {'morpheme':u'ね', 'base':u'ね', 'reading': 
                u'ね', 'position': 21, 'length': 3, 
                'type':japanese_parser.PARTICLE}
        ]
    },
    {
        'expression':u'明日は今日よりやや暖かいでしょう.',
        'reading':u'明日[あした]は 今日[きょう]よりやや 暖[あたた]かいでしょう.',
        'components':[
            {'morpheme':u'明日', 'length':6, 'base':u'明日', 
                'position':0, 'reading':u'あした', 
                'type':japanese_parser.NOUN},
            {'morpheme':u'は', 'length':3, 'base':u'は', 
                'position':6, 'reading':u'は', 
                'type':japanese_parser.PARTICLE},
            {'morpheme':u'今日', 'length':6, 'base':u'今日', 
                'position':9, 'reading':u'きょう', 
                'type':japanese_parser.NOUN},
            {'morpheme':u'より', 'length':6, 'base':u'より', 
                'position':15, 'reading':u'より', 
                'type':japanese_parser.PARTICLE},
            {'morpheme':u'やや', 'length':6, 'base':u'やや', 
                'position':21, 'reading':u'やや', 
                'type':japanese_parser.ADVERB},
            {'morpheme':u'暖かい', 'length':9, 'base':u'暖かい', 
                'position':27, 'reading':u'あたたかい', 
                'type':japanese_parser.ADJECTIVE},
            {'morpheme':u'でしょ', 'length':9, 'base':u'です', 
                'position':36, 'reading':u'でしょ', 
                'type':japanese_parser.AUXILIARY_VERB},
            {'morpheme':u'う', 'length':3, 'base':u'う', 
                'position':45, 'reading':u'う', 
                'type':japanese_parser.AUXILIARY_VERB},
            {'morpheme':u'.', 'length':1, 'base':u'', 
                'position':48, 'reading':u'', 
                'type':japanese_parser.NOUN} 
        ]
    },
    {
        'expression':u'  彼は目が細い.',
        'reading':u'彼[かれ]は 目[め]が 細[ほそ]い.',
        'components':[
            {'morpheme':u'彼', 'length':3, 'base':u'彼', 
                'position':2, 'reading':u'かれ', 
                'type':japanese_parser.NOUN, },
            {'morpheme':u'は', 'length':3, 'base':u'は', 
                'position':5, 'reading':u'は', 
                'type':japanese_parser.PARTICLE, },
            {'morpheme':u'目', 'length':3, 'base':u'目', 
                'position':8, 'reading':u'め', 
                'type':japanese_parser.NOUN, },
            {'morpheme':u'が', 'length':3, 'base':u'が', 
                'position':11, 'reading':u'が', 
                'type':japanese_parser.PARTICLE, },
            {'morpheme':u'細い', 'length':6, 'base':u'細い', 
                'position':14, 'reading':u'ほそい', 
                'type':japanese_parser.ADJECTIVE, },
            {'morpheme':u'.', 'length':1, 'base':u'', 
                'position':20, 'reading':u'', 
                'type':japanese_parser.NOUN, },
        ]
    },
    {
        'expression':u'This is english',
        'reading':u'This is english',
        'components':[
            {'morpheme':u'This', 'length':4, 'base':u'', 
                'position':0, 'reading':u'', 'type':japanese_parser.NOUN, },
            {'morpheme':'is', 'length':2, 'base':'', 
                'position':5, 'reading':'', 'type':japanese_parser.NOUN, },
            {'morpheme':u'english', 'length':7, 'base':u'',
                'position':8, 'reading':u'', 'type':japanese_parser.NOUN, },
        ]
    },
    {
        'expression':u'プログラムは一部2,000 円だ.',
        'reading':u'プログラムは 一部[いちぶ] 2, 000 円[えん]だ.',
        'components':[
            {'morpheme':u'プログラム', 'length':15, 'base':u'プログラム', 'position':0, 'reading':u'ぷろぐらむ', 'type':japanese_parser.NOUN, },
            {'morpheme':u'は', 'length':3, 'base':u'は', 
                'position':15, 'reading':u'は', 
                'type':japanese_parser.PARTICLE, },
            {'morpheme':u'一部', 'length':6, 'base':u'一部', 
                'position':18, 'reading':u'いちぶ', 
                'type':japanese_parser.NOUN, },
            {'morpheme':u'2', 'length':1, 'base':u'', 
                'position':24, 'reading':u'', 
                'type':japanese_parser.NOUN, },
            {'morpheme':u',', 'length':1, 'base':u'', 
                'position':25, 'reading':u'', 
                'type':japanese_parser.NOUN, },
            {'morpheme':u'000', 'length':3, 'base':u'', 
                'position':26, 'reading':u'', 
                'type':japanese_parser.NOUN, },
            {'morpheme':u'円', 'length':3, 'base':u'円', 
                'position':30, 'reading':u'えん', 
                'type':japanese_parser.NOUN, },
            {'morpheme':u'だ', 'length':3, 'base':u'だ', 
                'position':33, 'reading':u'だ', 
                'type':japanese_parser.AUXILIARY_VERB, },
            {'morpheme':u'.', 'length':1, 'base':u'', 
                'position':36, 'reading':u'', 
                'type':japanese_parser.NOUN, },
        ]
    },
    {
        'expression':u'データは以下のとおりです。',
        'reading':u'データは 以下[いか]のとおりです。',
        'components':[
            {'morpheme':u'データ', 'length':9, 'base':u'データ', 
                'position':0, 'reading':u'でーた', 
                'type':4, },
            {'morpheme':u'は', 'length':3, 'base':u'は', 
                'position':9, 'reading':u'は', 
                'type':7, },
            {'morpheme':u'以下', 'length':6, 'base':u'以下', 
                'position':12, 'reading':u'いか', 
                'type':4, },
            {'morpheme':u'の', 'length':3, 'base':u'の', 
                'position':18, 'reading':u'の', 
                'type':7, },
            {'morpheme':u'とおり', 'length':9, 'base':u'とおり', 
                'position':21, 'reading':u'とおり', 
                'type':4, },
            {'morpheme':u'です', 'length':6, 'base':u'です', 
                'position':30, 'reading':u'です', 
                'type':5, },
        ]
    },
]

class MyTest(unittest.TestCase):

    def testExpressions(self):
        parser = japanese_parser.JapaneseParser()
        for idx, e in enumerate(expected):
            expression = e['expression']
            results = parser.parse(expression)
            gotComp = results.components
            wantComp = e['components']
            self.assertEqual(gotComp, wantComp, 
                "E{}: Parse components mismatch\nGot:\n{}\n\nWant:\n{}".format(idx, japanese_parser.listDictString(gotComp), japanese_parser.listDictString(wantComp)))
        #self.assertEqual(results.ankiReading(), expectedAnkiReading1, "parse anki readings mismatch")

if __name__ == '__main__':
    unittest.main()
