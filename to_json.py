import json


ar = []

with open('cenz.txt', encoding='utf-8') as doc:
    for s in doc:
        low = s.lower().split('\n')[0]
        if low != '':
            ar.append(low)

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)