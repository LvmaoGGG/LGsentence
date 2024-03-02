import requests
import json

www = 'http://open.saintic.com/api/sentence/'


def get_api(www):
    api = requests.get(www)

    return api.json()

    with open(api.json) as f:
        data = json.load(f)

    return data


a = json.dumps(get_api(www))
b = json.loads(a)
name = b['data']['name']
sentence = b['data']['sentence']

ruslut = f'''{sentence} 
\t---《{name}》
'''
