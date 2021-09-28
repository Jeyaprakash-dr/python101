data = [
    {
        'word':'disaster',
        'phonetic':'dɪˈzɑːstə',
        'phonetics':
            [
                {
                    'text':'dɪˈzɑːstə',
                    'audio':'//ssl.gstatic.com/dictionary/static/sounds/20200429/disaster--_gb_1.mp3'
                    }
                ],
        'origin':'mid 16th century: from Italian disastro ‘ill-starred event’, from dis- (expressing negation) + astro ‘star’ (from Latin astrum ).',
        'meanings':
            [
                {
                    'partOfSpeech':'noun',
                    'definitions':
                        [
                            {
                                'definition':'a sudden accident or a natural catastrophe that causes great damage or loss of life.',
                                'example':'159 people died in the disaster',
                                'synonyms':['catastrophe', 'calamity', 'cataclysm', 'tragedy', 'act of God',
                                            'holocaust', 'accident', 'mishap', 'misadventure', 'mischance',
                                            'setback', 'reversal', 'reverse of fortune', 'contretemps',
                                            'stroke of ill luck', 'problem', 'difficulty', 'heavy blow',
                                            'shock', 'buffet', 'adversity', 'trouble', 'misfortune', 'ruin',
                                            'ruination', 'tribulation', 'woe', 'distress', 'casualty', 'bale',
                                            'mishanter'],
                                'antonyms':['blessing']

                                }
                            ]
                    }
                ]
        }
    ]

for i in data:
    print(i['word'])
    for j in i['phonetics']:
        for k, v in j.keys(), j.values():
            print(k, v)
        print("Phonetics: \n \t" + j['text'])
        for k in i['meanings']:
            for m in k['definitions']:
                for n in m['antonyms']:
                    print("%s \t" % n)

data2 = [{
     'word':'miraculous',
     'phonetic':'mɪˈrakjʊləs',
     'phonetics':[{
                      'text':'mɪˈrakjʊləs',
                      'audio':'//ssl.gstatic.com/dictionary/static/sounds/20200429/miraculous--_gb_1.8.mp3'
                      }],
     'origin':'late Middle English: from French miraculeux or medieval Latin miraculosus, from Latin miraculum (see miracle).',
     'meanings':[{
                     'partOfSpeech':'adjective',
                     'definitions':[{
                                        'definition':'of the nature of a miracle or having the power to work miracles.',
                                        'example':'a miraculous cure',
                                        'synonyms':['supernatural', 'preternatural', 'superhuman', 'inexplicable',
                                                    'unaccountable', 'fantastic', 'magical', 'phenomenal', 'prodigious',
                                                    'thaumaturgic'],
                                        'antonyms':[]
                                        }]
                     }]
     }]


