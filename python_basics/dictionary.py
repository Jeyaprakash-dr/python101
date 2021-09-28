import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        user_input = input("Did you mean %s instead?Enter Y if yes, or N if no: "% get_close_matches(w, data.keys())[0])
        if user_input == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif user_input == "N":
            return "The word doesn't exists. Please search for correct word"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exists. Please search for correct word"


word = input("Enter a word to search: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
