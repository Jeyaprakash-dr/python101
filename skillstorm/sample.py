var = [{
    'word': 'disaster', 'phonetic': 'dɪˈzɑːstə', 'phonetics': [
        {'text': 'dɪˈzɑːstə', 'audio': '//ssl.gstatic.com/dictionary/static/sounds/20200429/disaster--_gb_1.mp3'}],
    'origin': 'mid 16th century: from Italian disastro ‘ill-starred event’, from dis- (expressing negation) + astro ‘star’ (from Latin astrum ).',
    'meanings': [{
        'partOfSpeech': 'noun', 'definitions': [
            {
                'definition': 'a sudden accident or a natural catastrophe that causes great damage or loss of life.',
                'example': '159 people died in the disaster',
                'synonyms': ['catastrophe', 'calamity', 'cataclysm', 'tragedy', 'act of God', 'holocaust', 'accident',
                             'mishap',
                             'misadventure', 'mischance', 'setback', 'reversal', 'reverse of fortune', 'contretemps',
                             'stroke of ill luck', 'problem', 'difficulty', 'heavy blow', 'shock', 'buffet',
                             'adversity',
                             'trouble', 'misfortune', 'ruin', 'ruination', 'tribulation', 'woe', 'distress',
                             'casualty', 'bale',
                             'mishanter'], 'antonyms': ['blessing']
            }]
    }]
}]



for obj in var:
    print(obj['word'])
    for mean in obj['meanings']:
        print(mean)



echo "sapmsRP1        3602/tcp        # SAP System Message Server Port" >> /etc/services
grep -i sapmsRP1 /etc/services
