#!/usr/bin/env python
# -*- coding: utf-8 -*-

from noj.data_structures import *

SAMPLE_ENTRIES_1 = list()

e = DictionaryEntry(u'\u304a\u3068\u3053\u308d', [u'\u5fa1\u6240'], u'')
m = DictionaryMeaning(u'\u3014\u76f8\u624b\u306e\u4f4f\u6240\u3092\u6307\u3057\u3066\u3015 your address.', 1)
ue = UsageExample(u'\u305d\u3053\u306b\u3042\u306a\u305f\u306e\u304a\u3068\u3053\u308d\u3068\u304a\u540d\u524d\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044.', u'Please write your name and address there.', 0)
m.add_usage_example(ue)
e.add_meaning(m)
SAMPLE_ENTRIES_1.append(e)
