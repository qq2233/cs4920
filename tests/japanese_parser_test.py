# -*- coding: utf-8 -*-
import unittest
from noj import japanese_parser

expected = [
    {
        'expression':'今日もしないとね。',
        'reading':'今日[きょう]もしないとね。',
        'components':[
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
    },
    {
        'expression':'明日は今日よりやや暖かいでしょう.',
        'reading':'明日[あした]は 今日[きょう]よりやや 暖[あたた]かいでしょう.',
        'components':[
            {'morpheme':'明日', 'length':6, 'base':'明日', 
                'position':0, 'reading':'あした', 
                'type':japanese_parser.NOUN},
            {'morpheme':'は', 'length':3, 'base':'は', 
                'position':6, 'reading':'は', 
                'type':japanese_parser.PARTICLE},
            {'morpheme':'今日', 'length':6, 'base':'今日', 
                'position':9, 'reading':'きょう', 
                'type':japanese_parser.NOUN},
            {'morpheme':'より', 'length':6, 'base':'より', 
                'position':15, 'reading':'より', 
                'type':japanese_parser.PARTICLE},
            {'morpheme':'やや', 'length':6, 'base':'やや', 
                'position':21, 'reading':'やや', 
                'type':japanese_parser.ADVERB},
            {'morpheme':'暖かい', 'length':9, 'base':'暖かい', 
                'position':27, 'reading':'あたたかい', 
                'type':japanese_parser.ADJECTIVE},
            {'morpheme':'でしょ', 'length':9, 'base':'です', 
                'position':36, 'reading':'でしょ', 
                'type':japanese_parser.AUXILIARY_VERB},
            {'morpheme':'う', 'length':3, 'base':'う', 
                'position':45, 'reading':'う', 
                'type':japanese_parser.AUXILIARY_VERB},
            {'morpheme':'.', 'length':1, 'base':'', 
                'position':48, 'reading':'', 
                'type':japanese_parser.NOUN} 
        ]
    },
    {
        'expression':'  彼は目が細い.',
        'reading':'彼[かれ]は 目[め]が 細[ほそ]い.',
        'components':[
            {'morpheme':'彼', 'length':3, 'base':'彼', 
                'position':2, 'reading':'かれ', 
                'type':japanese_parser.NOUN, },
            {'morpheme':'は', 'length':3, 'base':'は', 
                'position':5, 'reading':'は', 
                'type':japanese_parser.PARTICLE, },
            {'morpheme':'目', 'length':3, 'base':'目', 
                'position':8, 'reading':'め', 
                'type':japanese_parser.NOUN, },
            {'morpheme':'が', 'length':3, 'base':'が', 
                'position':11, 'reading':'が', 
                'type':japanese_parser.PARTICLE, },
            {'morpheme':'細い', 'length':6, 'base':'細い', 
                'position':14, 'reading':'ほそい', 
                'type':japanese_parser.ADJECTIVE, },
            {'morpheme':'.', 'length':1, 'base':'', 
                'position':20, 'reading':'', 
                'type':japanese_parser.NOUN, },
        ]
    },
    {
        'expression':'This is english',
        'reading':'This is english',
        'components':[
            {'morpheme':'This', 'length':4, 'base':'', 
                'position':0, 'reading':'', 'type':japanese_parser.NOUN, },
            {'morpheme':'is', 'length':2, 'base':'', 
                'position':5, 'reading':'', 'type':japanese_parser.NOUN, },
            {'morpheme':'english', 'length':7, 'base':'',
                'position':8, 'reading':'', 'type':japanese_parser.NOUN, },
        ]
    },
    {
        'expression':'プログラムは一部2,000 円だ.',
        'reading':'プログラムは 一部[いちぶ] 2, 000 円[えん]だ.',
        'components':[
            {'morpheme':'プログラム', 'length':15, 'base':'プログラム', 'position':0, 'reading':'ぷろぐらむ', 'type':japanese_parser.NOUN, },
            {'morpheme':'は', 'length':3, 'base':'は', 
                'position':15, 'reading':'は', 
                'type':japanese_parser.PARTICLE, },
            {'morpheme':'一部', 'length':6, 'base':'一部', 
                'position':18, 'reading':'いちぶ', 
                'type':japanese_parser.NOUN, },
            {'morpheme':'2', 'length':1, 'base':'', 
                'position':24, 'reading':'', 
                'type':japanese_parser.NOUN, },
            {'morpheme':',', 'length':1, 'base':'', 
                'position':25, 'reading':'', 
                'type':japanese_parser.NOUN, },
            {'morpheme':'000', 'length':3, 'base':'', 
                'position':26, 'reading':'', 
                'type':japanese_parser.NOUN, },
            {'morpheme':'円', 'length':3, 'base':'円', 
                'position':30, 'reading':'えん', 
                'type':japanese_parser.NOUN, },
            {'morpheme':'だ', 'length':3, 'base':'だ', 
                'position':33, 'reading':'だ', 
                'type':japanese_parser.AUXILIARY_VERB, },
            {'morpheme':'.', 'length':1, 'base':'', 
                'position':36, 'reading':'', 
                'type':japanese_parser.NOUN, },
        ]
    },
    {
        'expression':'データは以下のとおりです。',
        'reading':'データは 以下[いか]のとおりです。',
        'components':[
            {'morpheme':'データ', 'length':9, 'base':'データ', 
                'position':0, 'reading':'でーた', 
                'type':4, },
            {'morpheme':'は', 'length':3, 'base':'は', 
                'position':9, 'reading':'は', 
                'type':7, },
            {'morpheme':'以下', 'length':6, 'base':'以下', 
                'position':12, 'reading':'いか', 
                'type':4, },
            {'morpheme':'の', 'length':3, 'base':'の', 
                'position':18, 'reading':'の', 
                'type':7, },
            {'morpheme':'とおり', 'length':9, 'base':'とおり', 
                'position':21, 'reading':'とおり', 
                'type':4, },
            {'morpheme':'です', 'length':6, 'base':'です', 
                'position':30, 'reading':'です', 
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
