import requests
import pandas as pd

import json
import csv


id = input('Whats The id ')
page = input(" page number ")
req = requests.get("https://gdbrowser.com/api/comments/"+id+"?page="+page)
jsons = req.text

f = open("output.json", "w")
f.write(jsons)
f.close()
df = pd.read_json (r'./output.json')
df.to_csv (r'./output.csv', index = None)