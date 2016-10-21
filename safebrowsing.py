#!/usr/bin/python

import requests

proxy={'http':'<your proxy here>','https':'<your proxy here>'}
headers={'Content-Type':'application/json'}

payload={
    "client": {
      "clientId":      "me",
      "clientVersion": "1"
    },
    "threatInfo": {
      "threatTypes":      ["THREAT_TYPE_UNSPECIFIED","MALWARE","SOCIAL_ENGINEERING","UNWANTED_SOFTWARE","POTENTIALLY_HARMFUL_APPLICATION"],
      "platformTypes":    ["ALL_PLATFORMS"],
      "threatEntryTypes": ["THREAT_ENTRY_TYPE_UNSPECIFIED","URL","EXECUTABLE","IP_RANGE"],
      "threatEntries": [
        {"url": "http://www.github.com/"},
        {"url": "http://www.porn.com/"},
        {"url": "http://www.stopmeagency.free.fr/"}
      ]
    }
  }

r=requests.post('https://safebrowsing.googleapis.com/v4/threatMatches:find?key=<your google API key>',headers=headers,json=payload,proxies=proxy)
print r.text
