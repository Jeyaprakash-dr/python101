# [{
#     'word':'miraculous',
#     'phonetic':'mɪˈrakjʊləs',
#     'phonetics':[{
#         'text':'mɪˈrakjʊləs',
#         'audio': '//ssl.gstatic.com/dictionary/static/sounds/20200429/miraculous--_gb_1.8.mp3'
#     }],
#     'origin':'late Middle English: from French miraculeux or medieval Latin miraculosus, from Latin miraculum '
#              '(see miracle).',
#     'meanings':[{
#         'partOfSpeech':'adjective',
#         'definitions':[{
#             'definition':'of the nature of a miracle or having the power to work miracles.',
#             'example':'a miraculous cure',
#             'synonyms':['supernatural','preternatural','superhuman','inexplicable',
#                         'unaccountable','fantastic','magical','phenomenal','prodigious',
#                         'thaumaturgic'],
#             'antonyms':[]
#         }]
#     }]
# }]

import requests
import json

url = "https://api.dictionaryapi.dev/api/v2/entries/en/usa"
out = requests.get(url)
result = json.loads(out.text)

for i in result:
    print("Word: ", i['word'])
    print("Phonetic: ", i['phonetic'])
    for j in i['phonetics']:
        print("Phonetics Text: ", j['text'])
        print("Phonetics Audio: ", j['audio'])
    print("Origin: ", i['origin'] if i['origin'] in i else "None")
    for k in i['meanings']:
        print("Part of Speech: ", k['partOfSpeech'])
        for m in k['definitions']:
            print("Definition: ", m['definition'])
            print("Example: ", m['example'] if list(m['example']) == 0 else "None")
            print("Synonyms: ", m['synonyms'] if list(m['synonyms']) == 0 else "None")
            print("Antonyms: ", m['antonyms'] if list(m['antonyms']) == 0 else "None")

data4 = [
    {
        "word": "USA",
        "phonetic": "juːɛsˈeɪ",
        "phonetics": [
            {
                "text": "juːɛsˈeɪ",
                "audio": "//ssl.gstatic.com/dictionary/static/sounds/20200429/usa--_gb_1.mp3"
            }
        ],
        "meanings": [
            {
                "partOfSpeech": "abbreviation",
                "definitions": [
                    {
                        "definition": "United States of America.",
                        "synonyms": [],
                        "antonyms": []
                    },
                    {
                        "definition": "United States Army.",
                        "synonyms": [],
                        "antonyms": []
                    }
                ]
            }
        ]
    }
]


word2 = [
  {
    'word': 'believe',
    'phonetic': 'bɪˈliːv',
    'phonetics': [
      {
        'text': 'bɪˈliːv',
        'audio': '//ssl.gstatic.com/dictionary/static/sounds/20200429/believe--_gb_1.mp3'
      }
    ],
    'origin': 'late Old English belȳfan, belēfan, alteration of gelēfan, of Germanic origin; related to Dutch geloven '
              'and German glauben, also to lief.',
    'meanings': [
      {
        'partOfSpeech': 'verb',
        'definitions': [
          {
            'definition': 'accept that (something) is true, especially without proof.',
            'example': "the superintendent believed Lancaster's story",
            'synonyms': [
              'be convinced by',
              'trust',
              'have confidence in',
              'consider honest',
              'consider truthful',
              'regard as true',
              'accept as true',
              'accept',
              'give credence to',
              'credit',
              'give credit to',
              'put confidence in',
              'count on',
              'rely on',
              'depend on',
              'swallow',
              'swallow something hook',
              'line',
              'and sinker',
              'fall for',
              'go for',
              'buy',
              'take as gospel'
            ],
            'antonyms': [
              'disbelieve'
            ]
          },
          {
            'definition': 'hold (something) as an opinion; think.',
            'example': "I believe we've already met",
            'synonyms': [
              'think',
              'be of the opinion that',
              'think it likely that',
              'have an idea that',
              'imagine',
              'feel',
              'have a feeling',
              'hold',
              'maintain',
              'suspect',
              'suppose',
              'assume',
              'presume',
              'conjecture',
              'surmise',
              'postulate that',
              'theorize that',
              'conclude',
              'come to the conclusion that',
              'deduce',
              'understand',
              'be given to understand',
              'take it',
              'gather',
              'fancy',
              'guess',
              'dare say',
              'figure',
              'reckon',
              'ween'
            ],
            'antonyms': [
              'doubt'
            ]
          }
        ]
      }
    ]
  }
]

data5 = {
  "data": [
    {
      "attributes": {
        "active_period": [
          {
            "end": "2021-11-01T02:30:00-04:00",
            "start": "2021-08-29T04:30:00-04:00"
          }
        ],
        "banner": "null",
        "cause": "UNKNOWN_CAUSE",
        "created_at": "2021-08-25T21:40:52-04:00",
        "description": "null",
        "effect": "SERVICE_CHANGE",
        "header": "Effective August 29: Red Line frequency increases throughout the day on weekdays.",
        "informed_entity": [
          {
            "activities": [
              "BOARD",
              "EXIT",
              "RIDE"
            ],
            "route": "Red",
            "route_type": 1
          }
        ],
        "lifecycle": "ONGOING",
        "service_effect": "Red Line notice",
        "severity": 3,
        "short_header": "Effective August 29: Red Line frequency increases throughout the day on weekdays.",
        "timeframe": "through October 31",
        "updated_at": "2021-08-25T21:40:52-04:00",
        "url": "null"
      },
      "id": "402137",
      "links": {
        "self": "/alerts/402137"
      },
      "type": "alert"
    }
  ],
  "jsonapi": {
    "version": "1.0"
  }
}
