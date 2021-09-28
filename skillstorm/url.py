import requests
import json
import pandas

# post_id = input('enter a word: ')
# url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+post_id
#
# response = requests.get(url, params={'word': post_id})
# result = json.loads(response.text)
# print(result['word'])

url = "https://api.dictionaryapi.dev/api/v2/entries/en/believe"
out = requests.get(url)
print(type(out))
result = json.loads(out.text)
# for lis in result:
#     for i in lis:
#         print(i)
# print(type(result))
print(result)

for i in result:
    print(i['word'])
    for j in i['phonetics']:
        print(j.keys(), j.values())
        print("Phonetics: \n \t" + j['text'])
        for k in i['meanings']:
            for m in k['definitions']:
                for n in m['antonyms']:
                    print("%s \t" % n)

# response = requests.get(url)
# parsing the json from HTTP response body and convert into dict
# comments = json.loads(response.text)
# print(comments)
# incomplete_todos = 0
#
# for todo in todos:
#     if not todo['completed']:
#         incomplete_todos += 1
#
#
# print(incomplete_todos)
#
# title = input('Enter todo lite: ')
#
# url = "https://jsonplaceholder.typicode.com/todos/115"
# request_body = {
#     "userId": 2012,
#     "id": 7,
#     "title": title,
#     "completed": True
# }
#
# response = requests.put(url, json=request_body)
# todo = json.loads(response.text)
# print(todo)
#
# response = requests.get(url)
# print(response.status_code)
# print(response.headers['Content-Encoding'])
#
#  data = [{'word': 'disaster', 'phonetic': 'dɪˈzɑːstə', 'phonetics': [
#     {'text': 'dɪˈzɑːstə', 'audio': '//ssl.gstatic.com/dictionary/static/sounds/20200429/disaster--_gb_1.mp3'}],
#         'origin': 'mid 16th century: from Italian disastro ‘ill-starred event’, from dis- (expressing negation) + '
#                   'astro ‘star’ (from Latin astrum ).',
#         'meanings': [{'partOfSpeech': 'noun', 'definitions': [
#             {'definition': 'a sudden accident or a natural catastrophe that causes great damage or loss of life.',
#              'example': '159 people died in the disaster',
#              'synonyms': ['catastrophe', 'calamity', 'cataclysm', 'tragedy', 'act of God', 'holocaust', 'accident',
#                           'mishap', 'misadventure', 'mischance', 'setback', 'reversal', 'reverse of fortune',
#                           'contretemps', 'stroke of ill luck', 'problem', 'difficulty', 'heavy blow', 'shock', 'buffet',
#                           'adversity', 'trouble', 'misfortune', 'ruin', 'ruination', 'tribulation', 'woe', 'distress',
#                           'casualty', 'bale', 'mishanter'], 'antonyms': ['blessing']}]}]}]
