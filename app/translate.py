import json
import requests
from flask import current_app
from flask_babel import _

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&from=' + source_language + '&to=' + dest_language
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Content-type': 'application/json'
    }

    body = [{
        'text' : text
    }]

    r = requests.post(constructed_url, headers=headers, json=body)

    if r.status_code != 200:
        return _('Error: the translation service failed.')

    return r.json()[0]['translations'][0]['text']
